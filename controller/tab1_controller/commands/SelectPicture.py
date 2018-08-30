
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets
import cv2

import controller.tab1_controller.commands as commands
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import controller.supportingFunctions as Sp
import time
from PyQt5.QtWidgets import QDialog, QInputDialog
import model.container.getContainer as getContainer



class SelectPictureCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None, dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        print(self)
        print("book : ",self.context.current_book.book_folder_path)
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.gui, "Select Image", "",";Image Files (*.png);;Image Files (*.jpeg);;Image Files (*.jpg)")
            print(fileName)
            img = cv2.imread(fileName)
            img,dimen = self.context.SF.imageResize(img)
            cv2.imwrite("selectedImage.png",img)
            print('image saved')
            self.dialog.Page_view.setPixmap(QPixmap("selectedImage.png"))

        except Exception as e:
            print("  ", type(e).__name__)

    def unexcute(self):
        print(self)