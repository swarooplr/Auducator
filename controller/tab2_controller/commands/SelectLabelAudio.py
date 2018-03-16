
from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
class SelectLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context = context
        self.gui = gui



    def execute(self):
        print(self)
        try:
            print(self)
            _selected_label_index=str(self.gui.tab2_label_listwidget.currentRow())
            print(_selected_label_index)
            _label = self.get_selected_label(_selected_label_index)

            self.context.current_label=_label
            assert _label is not None
            self.load_label_info_to_ui()

        except Exception as e:
            print(e)
            pass


    def unexcute(self):
        print(self)


    def get_selected_label(self,_selected_label_index):
        if len(self.context.current_page.label_list) <= int(_selected_label_index):
            return None
        else:
            return self.context.current_page.label_list[int(_selected_label_index)]

    @inspector.bookselected
    @inspector.chapterselected
    def load_label_info_to_ui(self):
        _label=self.context.current_label
        if(_label.label_text is not None or
           not _label.label_text == ""):
                self.gui.tab2_label_input.setText(_label.label_text)

        if(_label.description_text is not None or
           not _label.description_text == ""):
                self.gui.tab2_description_input.setText(_label.description_text)

        if(_label.label_audio is not None or
           not _label.label_audio == ""):
                self.gui.tab2_label_audio_file.setText(_label.label_audio.split('/')[-1])

        if(_label.description_audio is not None or
           not _label.description_audio == ""):
                self.gui.tab2_description_audio_file.setText(_label.description_audio.split('/')[-1])

        """ load image here"""



class SelectAudioFileLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            self.get_audio_file()
        except:
            pass


    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def get_audio_file(self):
        file = (QtWidgets.QFileDialog.getOpenFileName(self.gui, "Select Book Folder"))[0]
        print(file)
        self.gui.tab2_label_audio_file.setText(file.split('/')[-1])



class SelectAudioFileDescribeCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            self.get_audio_file()
        except:
            pass


    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def get_audio_file(self):
        file = (QtWidgets.QFileDialog.getOpenFileName(self.gui, "Select Book Folder"))[0]
        print(file)
        self.gui.tab2_description_audio_file.setText(file.split('/')[-1])
