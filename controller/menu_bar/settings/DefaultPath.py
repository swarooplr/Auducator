import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog
import gui.choose_colour as choose_color
import json
from PyQt5 import QtCore, QtGui, QtWidgets

class DefaultPathSetting(settings.BaseSetting):

    def __init__(self,context = None, gui = None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        self.open_window()


    def unexcute(self):
        print(self)

    def open_window(self):


        self.preferences = json.load(open("../model/preferences.json", "r"))
        self.values = json.load(open("../model/values.json", "r"))

        self.w = self.AppWindow(self)
        self.w.setModal(True)

        self.w.show()

    def save_preference(self,colors):
        pass

    class AppWindow(QDialog):
        def __init__(self, MainUIRef):

            super().__init__()
            self.ui = choose_color.Ui_choose_colour()
            self.ui.setupUi(self,MainUIRef)


