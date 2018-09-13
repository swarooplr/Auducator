
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import imutils
import cv2
import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
import controller.exceptions.ExceptionHandler as exceptionhandler

class SelectLabelCommand(commands.BaseCommand):

    """
        Command to select audio label from filesystem
    """
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
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    def unexcute(self):
        print(self)


    def get_selected_label(self,_selected_label_index):
        """

        :param _selected_label_index: index of selected label from listwidget
        :type _selected_label_index: int
        :return: corresponding label object
        :rtype: Label
        """
        if len(self.context.current_page.label_list) <= int(_selected_label_index):
            return None
        else:
            return self.context.current_page.label_list[int(_selected_label_index)]

    @inspector.bookselected
    @inspector.chapterselected
    def load_label_info_to_ui(self):
        """
        Loads all the information related to label into the UI fields
        :return:
        :rtype: None
        """
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
        #print("starting image read")
        img = cv2.imread(self.context.current_page.page_file_path+"\\"+self.context.current_page.page_image_name)
        #cv2.imshow("lol1", img)
        crop_img = img[int(_label.y1):int(_label.y2),int(_label.x1):int(_label.x2)]
<<<<<<< HEAD
        print("image cropped")
=======
        #print("image cropped")
>>>>>>> 412b754793d8f1878cea1ed79f7e47792e0abbf2
        #cv2.imshow("lol",crop_img)

        h = self.gui.tab2_label_preview.frameGeometry().height()
        w = self.gui.tab2_label_preview.frameGeometry().width()
        image = imutils.resize(crop_img, height=h, width=w)
        print("sizes = ",h,w)

        cv2.imwrite("cropped_image.png", image)

        self.gui.tab2_label_preview.setPixmap(QPixmap("cropped_image.png"))



class SelectAudioFileLabelCommand(commands.BaseCommand):

    """
        Command to select audio label from filesystem
    """

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            self.get_audio_file()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def get_audio_file(self):
        """
        Loads the file name of the selected audio file on UI text field
        :return:
        :rtype: None
        """
        file = (QtWidgets.QFileDialog.getOpenFileName(self.gui, "Select Book Folder"))[0]
        print(file)
        self.gui.tab2_label_audio_file.setText(file)



class SelectAudioFileDescribeCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            self.get_audio_file()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
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
        self.gui.tab2_description_audio_file.setText(file)
