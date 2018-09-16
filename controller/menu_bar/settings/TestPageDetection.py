from PyQt5.QtCore import QDir

import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog
import cv2
from PyQt5.QtWidgets import QMessageBox
import json
import controller.supportingFunctions as supporting_functions
import controller.VisionModules as VM
from PyQt5 import QtCore, QtGui, QtWidgets

class TestPageDetectionSetting(settings.BaseSetting):

    def __init__(self,context = None, gui = None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        try:
            self.start()
        except Exception as e:
            print(type(e).__doc__)


    def unexcute(self):
        print(self)

    def start(self):
        img = None
        self.SF = supporting_functions.supportingFunctions(self.context)
        self.VM = VM.VisionModules(self.SF)
        try:
            img = self.VM.pageSelector()
            cv2.imshow("test : ",img)
        except:
            if img == None:
                QMessageBox.about(self.gui, "Error", "No camera detected, \nPlease try changing the camera port in settings ")
                print("camera error")
            print("error")




