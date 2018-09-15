from PyQt5.QtCore import QDir

import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog

import json
from PyQt5 import QtCore, QtGui, QtWidgets

class DefaultPathSetting(settings.BaseSetting):

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

        file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Folder as default path"))
        #text, ok = QInputDialog.getText(self.gui, 'Default Path', '\nEnter the default path for books:                 .\n')

        print(file)
        if file != "":
            #fname = QDir.toNativeSeparators(file + "/")
            self.preferences['book_path'] = file

            data = json.dumps(self.preferences)
            print(data)
            with open("preferences.json", "w") as f:
                f.write(data)



