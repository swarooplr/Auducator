import controller.tab1_controller.commands as commands
import cv2
import numpy as np
import imutils
import controller.supportingFunctions as Sp
from PyQt5.QtGui import QIcon, QPixmap
import cv2


class RotatePageCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
       print(self)

    def unexcute(self):
        print(self)