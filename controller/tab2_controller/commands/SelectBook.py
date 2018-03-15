
from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
import model.container.getContainer as getContainer


class SelectBookCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Book Folder"))
            print(file)
            #check if valid book

            __bookname=file.split('/')[-1]
            self.gui.tab2_book_name_2.setText(__bookname)
            getContainer.loadBook(file)
            self.context.set_current_book(__bookname)






        except:
            pass



    def unexcute(self):
        print(self)


        











