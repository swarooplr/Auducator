import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog
import gui.menu_bar.chooseResolution as choose_resolution
import json
from functools import  partial
from PyQt5 import QtCore, QtGui, QtWidgets

class PictureSizeSetting(settings.BaseSetting):

    def __init__(self,context = None, gui = None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        try:
            self.open_window()
        except Exception as e:
            print(type(e).__doc__)


    def unexcute(self):
        print(self)

    def open_window(self):


        self.preferences = json.load(open("preferences.json", "r"))
        self.values = json.load(open("values.json", "r"))

        self.w = self.AppWindow(self.preferences,self.values)
        self.w.setModal(True)

        self.w.show()

    def save_preference(self,colors):
        pass

    class AppWindow(QDialog):
        def __init__(self,pref,val):

            super().__init__()
            self.values = val
            self.preferences = pref
            self.ui = choose_resolution.Ui_choose_resolution()
            self.ui.setupUi(self)

            r0 = self.values["resolutions"]["0"]
            r1 = self.values["resolutions"]["1"]
            r2 = self.values["resolutions"]["2"]

            self.ui.pushButton_3.setText(str(r0[0])+" X "+str(r0[1]))
            self.ui.pushButton.setText(str(r1[0])+" X "+str(r1[1]))
            self.ui.pushButton_2.setText(str(r2[0])+" X "+str(r2[1]))

            self.ui.pushButton_3.clicked.connect(partial(self.save_values,r0[0],r0[1]))
            self.ui.pushButton.clicked.connect(partial(self.save_values, r1[0], r1[1]))
            self.ui.pushButton_2.clicked.connect(partial(self.save_values, r2[0], r2[1]))

        def save_values(self,h,w):
            self.preferences["page_height"] = h
            self.preferences["page_width"] = w

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)

            self.close()




