import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
import controller.exceptions.ExceptionHandler as exceptionhandler

from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave


class StartRecordingCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui = gui



    def execute(self):
        try:
            self.start_record()
            pass
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def start_record(self):
        print("started")


        THRESHOLD = 500
        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        RATE = 44100

        def is_silent(snd_data):
            "Returns 'True' if below the 'silent' threshold"
            #return max(snd_data) < THRESHOLD

            # The function doesnt do what it is named after this is
            # what happens when you rip off from the internet and change stuff
            return not self.context.recording

        def normalize(snd_data):
            "Average the volume out"
            MAXIMUM = 16384
            times = float(MAXIMUM)/max(abs(i) for i in snd_data)

            r = array('h')
            for i in snd_data:
                r.append(int(i*times))
            return r

        def trim(snd_data):
            "Trim the blank spots at the start and end"
            def _trim(snd_data):
                snd_started = False
                r = array('h')

                for i in snd_data:
                    if not snd_started and abs(i)>THRESHOLD:
                        snd_started = True
                        r.append(i)

                    elif snd_started:
                        r.append(i)
                return r

            # Trim to the left
            snd_data = _trim(snd_data)

            # Trim to the right
            snd_data.reverse()
            snd_data = _trim(snd_data)
            snd_data.reverse()
            return snd_data

        def add_silence(snd_data, seconds):
            "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
            r = array('h', [0 for i in range(int(seconds*RATE))])
            r.extend(snd_data)
            r.extend([0 for i in range(int(seconds*RATE))])
            return r

        def record():
            """
            Record a word or words from the microphone and
            return the data as an array of signed shorts.

            Normalizes the audio, trims silence from the
            start and end, and pads with 0.5 seconds of
            blank sound to make sure VLC et al can play
            it without getting chopped off.
            """
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT, channels=1, rate=RATE,
                input=True, output=True,
                frames_per_buffer=CHUNK_SIZE)

            num_silent = 0
            snd_started = False

            r = array('h')

            while 1:
                # little endian, signed short
                snd_data = array('h', stream.read(CHUNK_SIZE))
                if byteorder == 'big':
                    snd_data.byteswap()
                r.extend(snd_data)

                silent = is_silent(snd_data)

                if silent and snd_started:
                    num_silent += 1
                elif not silent and not snd_started:
                    snd_started = True

                if snd_started and num_silent > 30:
                    break

            sample_width = p.get_sample_size(FORMAT)
            stream.stop_stream()
            stream.close()
            p.terminate()

            r = normalize(r)
            r = trim(r)
            r = add_silence(r, 0.5)
            return sample_width, r

        def record_to_file(path):
            "Records from the microphone and outputs the resulting data to 'path'"
            sample_width, data = record()
            data = pack('<' + ('h'*len(data)), *data)

            wf = wave.open(path, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(sample_width)
            wf.setframerate(RATE)
            wf.writeframes(data)
            wf.close()

        import glob
        import os

        try:
            dir = os.getcwd()

            for zippath in glob.iglob(os.path.join(dir, '*.wav')):
                try:
                    os.remove(zippath)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

        def initiate_recording():
            import random
            file_name = "recording" + str(random.getrandbits(5))+".wav"
            print("started recording...")
            self.context.recording = True

            record_to_file(file_name)
            print("ended recording...")
            self.gui.tab2_label_audio_file.setText(file_name)

        import threading
        try:
             threading.Thread(target=initiate_recording).start()
        except Exception as e:
                print(e)




    def unexecute(self):
        print(self)


class StopRecordingCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui = gui



    def execute(self):
        try:
            self.stop_record()
            pass
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def stop_record(self):
        print("stoped")
        self.context.recording = False

    def unexecute(self):
        print(self)


class PlayRecordingCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui = gui



    def execute(self):
        try:
            self.play_record()
            pass
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def play_record(self):
        print("playing...")
        from playsound import playsound
        file_name = self.gui.tab2_label_audio_file.text()
        try:
            file_name_to_play = self.context.current_page.page_file_path+"/"+file_name
            playsound(file_name_to_play)
        except:
            try:
                playsound(file_name)
            except Exception as e:
                print(e)
                pass



    def unexecute(self):
        print(self)

