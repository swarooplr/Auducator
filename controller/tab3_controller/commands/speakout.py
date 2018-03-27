import pyttsx3
from playsound import playsound
import controller.tab3_controller.commands.track as track


def speakout(voiceoverdetails,folderpath):
    print(voiceoverdetails)
    while True:
       # say=input("say it")
        #print(track.cordinates)
        elements=voiceoverdetails
        x=track.cordinates[0]
        y=track.cordinates[1]
        print(str(x)+","+str(y))
        for ele in voiceoverdetails:

             try:
                x1=ele.x1
                y1=ele.y1


                x4=ele.x2
                y4=ele.y2

                x2=ele.x2
                y2=ele.y1

                x3=ele.x1
                y3=ele.y2

                print(str(x1)+","+str(y1)+" "+str(x2)+","+str(y2)+" "+str(x3)+","+str(y3)+" "+str(x4)+","+str(y4))
                if(x1<x and x<x2 and y1<y and y<y3):
                    print("Match")
                    if(not ele.play_audio_label):
                          engine=pyttsx3.init()
                          engine.say(ele.label_text)
                          engine.runAndWait()
                    else:
                         print(folderpath+'/'+ele.label_audio)
                         playsound(folderpath+'/'+ele.label_audio)
                else:
                    print("No Matching Cordinates")
             except Exception as e:
                 print(e)
                 pass


