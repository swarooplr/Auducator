
from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab3_controller.commands as commands
import controller.tab3_controller.commands.ResetUI as reset_ui
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
            _book=getContainer.loadBook(file)
            self.gui.tab3_book_display.setText(_book.book_folder_path.split('/')[-1])
            self.gui.tab3_select_chapter_combobox.clear()
            for i in _book.chapter_list:
                self.gui.tab3_select_chapter_combobox.addItem(i.chapter_name)
                print(i.chapter_name)
            self.context.set_current_book(_book)
            print(self.context.current_book.book_folder_path)
            self.reset_context()

        except:
            pass

        self.reset_context()

    def unexcute(self):
        print(self)

    def reset_context(self):
        self.context.set_current_chapter(None)
        self.context.set_current_page(None)

        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()





        











