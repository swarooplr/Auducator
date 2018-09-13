import controller.menu_bar.settings as settings
from PyQt5.QtWidgets import QDialog, QInputDialog
import gui.menu_bar.customColour as custom_colour
import json
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

class CustomColourSetting(settings.BaseSetting):

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

        self.values = json.load(open("values.json", "r"))

        self.w = self.AppWindow(self.values)
        self.w.setModal(True)

        self.w.show()


    class AppWindow(QDialog):
        def __init__(self,values):

            super().__init__()


            self.ui = custom_colour.Ui_customColour()
            self.ui.setupUi(self)
            self.values = values
            self.ui.pushButton_2.clicked.connect(partial(self.save_values,"c1"))
            self.ui.pushButton_3.clicked.connect(partial(self.save_values,"c2"))

        def save_values(self,C):

            try:
                print(C)
                h = [int(self.ui.pu1.text().strip()),int(self.ui.pu2.text().strip()),int(self.ui.pu3.text().strip())]

                l = [int(self.ui.pl3.text().strip()), int(self.ui.pl3.text().strip()),int(self.ui.pl3.text().strip())]

                colour = dict()
                colour["high"] = h
                colour["low"] = l

                self.values["colours"][C] = colour
                print(self.values)

                data = json.dumps(self.values)
                print(data)
                with open("values.json", "w") as f:
                    f.write(data)

                self.close()

            except Exception as e:
                print(type(e).__doc__)


