import controller.tab1_controller.commands as commands
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog

import model.container.createContainer as createConatiner
import model as model
import model.container.getContainer as getContainer

import os

class NewBookCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Folder to create Book"))
        text, ok = QInputDialog.getText(self.gui, 'New Project',
                                        'Enter project name:')

        if ok:
            print(text)
            book_path = file + '/' + text
            try:
                _book = createConatiner.createBook(book_path)
                print(self.context)
                #self.context.set_current_book(_book)
                print('book path : ',book_path)

                _book = getContainer.loadBook(book_path)
                self.gui.tab1_book_name.setText(_book.book_folder_path.split('/')[-1])
                self.gui.tab1_chapter_name.setText("Default")
                self.gui.tab1_select_chapter_combobox.clear()

                for i in _book.chapter_list:
                    self.gui.tab1_select_chapter_combobox.addItem(i.chapter_name)
                    print(i.chapter_name)
                self.context.set_current_book(_book)
                print(self.context.current_book.book_folder_path)

            except:
                print('unable to create project at destination')

        print(file)

    def unexcute(self):
        print(self)


class NewChapterCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        text, ok = QInputDialog.getText(self.gui, 'New Chapter','Enter Chapter name:')
        if ok:
            try:
                chapter_path = self.context.current_book.book_folder_path+'/Config/'+text
                print("at : ", chapter_path)
                os.makedirs( chapter_path)
                self.context.current_book.add_chapter(model.container.Chapter(text,chapter_path,[]))
                #self.context.current_chapter = model.container.Chapter(text,chapter_path,[])
                self.gui.tab1_select_chapter_combobox.addItem(text)



            except:
                print("Couldnt create chapter")



    def unexcute(self):
        print(self)
