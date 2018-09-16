import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog

import json
from PyQt5 import QtCore, QtGui, QtWidgets

class ChooseCameraSetting(settings.BaseSetting):

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

        text, ok = QInputDialog.getText(self.gui, 'Camera number (port number)', '\nEnter a value between 0 to 4 \nCamera ID as in openCV :\n')

        if ok:
            self.preferences['camera'] = text

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)

