from PyQt5.QtCore import QDir

import controller.tab1_controller.commands as commands
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap

import time
import model.container.createContainer as createConatiner
import model as model
import model.container.getContainer as getContainer
import gui.tab1dialogUI as tab1Dialog
import os
import json
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.Inspectors as inspector
import controller.exceptions.ExceptionHandler as exceptionhandler

class NewBookCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui


    def execute(self):
        #print(self)

        self.preferences = json.load(open("preferences.json", "r"))

        if self.preferences['book_path'] == "":
            file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Folder to create Book"))
        else:
            file = self.preferences["book_path"]

        print(file)
        if not file == "":
            text, ok = QInputDialog.getText(self.gui, 'New Project','Enter project name:')

            if ok:
                print(text)
                book_path = os.path.join(file, text)
                try:
                    _book = createConatiner.createBook(book_path)

                    #print("book created at :" ,book_path, "   id:",_book)

                    print('book path : ',book_path)

                    _book = getContainer.loadBook(book_path)
                    self.gui.tab2_book_name_2.setText(_book.book_folder_path.split('/')[-1])
                    self.gui.tab2_chapter_select_combobox.clear()

                    print("book loaded . loading chapters "+ str(_book.chapter_list))

                    for i in _book.chapter_list:
                        self.gui.tab1_select_chapter_combobox.addItem(i.chapter_name)
                        print(i.chapter_name,"  ")

                    self.context.set_current_book(_book)
                    print(self.context.current_book.book_folder_path)
                    self.reset_context()



                except Exception as e:
                    print('Unable to create project at destination ' + type(e).__name__+ e.__doc__)

        print('Location not accessible')

    def unexcute(self):
        print(self)

    def reset_context(self):
        self.context.set_current_chapter(None)
        self.context.set_current_page(None)
        self.context.set_current_label(None)
        self.rest_ui = reset_ui.ResetUICommand(self.context, self.gui)
        self.rest_ui.execute()

class NewChapterCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui


    def execute(self):
        print(self)

        try:
            self.new_chapter()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e, self.gui).handle()
            print("Couldnt create chapter")

    def unexcute(self):
        print(self)

    @inspector.bookselected
    def new_chapter(self):
        text, ok = QInputDialog.getText(self.gui, 'New Chapter', 'Enter Chapter name:')
        if ok:

            chapter_path = os.path.join(self.context.current_book.book_folder_path, 'Config', text)
            print("at : ", chapter_path)
            os.makedirs(chapter_path)
            self.context.current_book.add_chapter(model.container.Chapter(text, chapter_path, []))
            # self.context.current_chapter = model.container.Chapter(text,chapter_path,[])
            self.gui.tab2_chapter_select_combobox.addItem(text)

class NewPageCommand(commands.BaseCommand):



    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui


    def execute(self):
        try:
            self.new_page()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e, self.gui).handle()
            pass


    def unexcute(self):
        pass

    @inspector.bookselected
    @inspector.chapterselected
    def new_page(self):
        print(self)
        self.w = self.AppWindow(self)
        # self.w.startDialog(self)
        self.w.setModal(True)
        self.w.show()

    class AppWindow(QDialog):
        def __init__(self,MainUIRef):
            super().__init__()
            self.ui = tab1Dialog.Ui_Dialog()
            self.ui.setupUi(self, MainUIRef)
            self.show()

