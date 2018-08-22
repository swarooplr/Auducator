
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets
import cv2

import controller.tab1_controller.commands as commands
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import time
from PyQt5.QtWidgets import QDialog, QInputDialog
import model.container.getContainer as getContainer



class SelectPictureCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        print("book : ",self.context.current_book.book_folder_path)
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.gui, "Select Image", "",";Image Files (*.png);;Image Files (*.jpeg);;Image Files (*.jpg)")
            print(fileName)
            cv2.imwrite("selectedImage.png",cv2.imread(fileName))
            print('image saved')
            self.gui.tab1_page_view.setPixmap(QPixmap("selectedImage.png"))

        except Exception as e:
            print("something sux  ", type(e).__name__)

    def unexcute(self):
        print(self)