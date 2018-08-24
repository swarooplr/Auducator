import controller.tab1_controller.commands as commands
import cv2
import numpy as np
import imutils
import controller.supportingFunctions as Sp
from PyQt5.QtGui import QIcon, QPixmap
import cv2


class RotatePageCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None,  dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        img = cv2.imread("selectedImage.png")
        frame = imutils.rotate_bound(img, 90)
        cv2.imwrite("selectedImage.png", frame)
        print('image saved')
        self.dialog.Page_view.setPixmap(QPixmap("selectedImage.png"))
        print(self)

    def unexcute(self):
        print(self)