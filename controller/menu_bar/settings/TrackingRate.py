import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog

import json
from PyQt5 import QtCore, QtGui, QtWidgets

class TrackingRateSetting(settings.BaseSetting):

    def __init__(self,context = None, gui = None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        self.open_window()


    def unexcute(self):
        print(self)

    def open_window(self):


        self.preferences = json.load(open("preferences.json", "r"))
        self.values = json.load(open("values.json", "r"))

        text, ok = QInputDialog.getText(self.gui, 'Tracking Rate', '\nEnter a value between 0 (highest) and 1000 (lowest) :\n')

        if ok:
            self.preferences['tracking_rate'] = text

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)

