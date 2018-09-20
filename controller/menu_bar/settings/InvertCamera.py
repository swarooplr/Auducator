import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog

import json
from PyQt5 import QtCore, QtGui, QtWidgets

class InvertCameraSetting(settings.BaseSetting):

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

        text, ok = QInputDialog.getText(self.gui, 'Invert Camera', '\nEnter a value  - 0 - 90 - 180 - 270 - 360')

        if ok:
            self.preferences['invert'] = text

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)

