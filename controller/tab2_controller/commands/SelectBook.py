
from PyQt5 import QtWidgets

import controller.tab2_controller.commands as commands
import controller.tab2_controller.commands.ResetUI as reset_ui
import model.container.getContainer as getContainer


class SelectBookCommand(commands.BaseCommand):
    """
      Command to execute after a book folder is selected,loads the corresponding chapters of the book into UI
    """

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Book Folder"))
            print(file)
            _book=getContainer.loadBook(file)
            self.gui.tab2_book_name_2.setText(_book.book_folder_path.split('/')[-1])
            self.gui.tab2_chapter_select_combobox.clear()
            for i in _book.chapter_list:
                self.gui.tab2_chapter_select_combobox.addItem(i.chapter_name)
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
        self.context.set_current_label(None)
        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()





        











