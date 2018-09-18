import controller.tab1_controller.commands as commands
import controller.tab1_controller.commands as commands
import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import imutils
from PyQt5.QtGui import QIcon, QPixmap
import controller.VisionModules as VM
import cv2

class TakePictureCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None, dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        print(self)
        img = None
        try:
            #print(self.context.current_book.book_folder_path)
            self.VM = VM.VisionModules(self.context.SF)
            img = self.VM.pageSelector()
            #cv2.imshow("img", img)

            cv2.imwrite("selectedImage.png", img)
            print('image saved')
            self.dialog.Page_view.setPixmap(QPixmap("selectedImage.png"))
        except Exception as e:
            if img == None:
                QMessageBox.about(self.gui, "Error", "No camera detected, \nPlease try changing the camera port in settings ")
                print("camera error")
            print("couldnt get page ",type(e).__doc__)

    def unexcute(self):
        print(self)





                    


