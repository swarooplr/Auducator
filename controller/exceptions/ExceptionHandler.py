
from PyQt5.QtWidgets import QMessageBox
import controller.exceptions as exceptions

class ExceptionHandler:
    def __init__(self, exception, gui=None):
        self.gui=gui
        self.exception=exception
        pass

    def handle(self):
        print(type(self.exception))

        if(type(self.exception) is exceptions.BookNotSelected):
            QMessageBox.about(self.gui, "Error", "Book Not selected")
        elif(type(self.exception) is exceptions.ChapterNotSelected):
            QMessageBox.about(self.gui, "Error", "Chapter Not selected")
        elif(type(self.exception) is exceptions.PageNotSelected):
            QMessageBox.about(self.gui, "Error", "Page Not selected")
        elif(type(self.exception) is exceptions.LabelNotSelected):
            QMessageBox.about(self.gui, "Error", "Label Not selected")
        else:
             QMessageBox.about(self.gui, "Error", "Error occurred")



