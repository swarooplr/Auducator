import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog
import gui.chooseColour as choose_color
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class ChooseColourSetting(settings.BaseSetting):

    def __init__(self,context = None, gui = None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        self.new_page()


    def unexcute(self):
        print(self)

    def new_page(self):


        self.preferences = json.load(open("preferences.json", "r"))

        self.w = self.AppWindow(self.preferences)
        self.w.setModal(True)

        self.w.show()

    def save_preference(self,colors):
        pass

    class AppWindow(QDialog):
        def __init__(self,pref):

            super().__init__()
            self.preferences = pref
            self.ui = choose_color.Ui_choose_colour()
            self.ui.setupUi(self)

            self.ui.pushButton.clicked.connect(partial(self.set_value,'c1','c2'))
            self.ui.pushButton_2.clicked.connect(partial(self.set_value,'c2','c1'))

        def set_value(self,c1,c2):

            self.preferences["colour1"] = c1
            self.preferences["colour2"] = c2

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)

            self.close()


