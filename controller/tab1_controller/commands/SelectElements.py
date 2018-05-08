
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


import controller.tab1_controller.commands as commands
import model.container.getContainer as getContainer



class SelectBookCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        try:
            file = str(QtWidgets.QFileDialog.getExistingDirectory(self.gui, "Select Book Folder"))
            print(file)
            _book = getContainer.loadBook(file)
            self.gui.tab1_book_name.setText(_book.book_folder_path.split('/')[-1])
            self.gui.tab1_select_chapter_combobox.clear()

            for i in _book.chapter_list:
                self.gui.tab1_select_chapter_combobox.addItem(i.chapter_name)
                print(i.chapter_name)
            self.context.set_current_book(_book)
            print(self.context.current_book.book_folder_path)
            #self.reset_context()

        except Exception as e:
            print(e)
            pass

        #self.reset_context()

    def unexcute(self):
        print(self)





class SelectChapterCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        try:
            print(self)
            #self.gui.tab2_page_listwidget.clear()
            _selected_chapter=str(self.gui.tab1_select_chapter_combobox.currentText())
            print("_selected chapter",_selected_chapter)
            _chapter=self.get_selected_chapter(_selected_chapter)
            print("chapter returned",len(_chapter.page_list))
            self.context.current_chapter=_chapter
            #assert _chapter is not None
            self.load_page_list_to_ui()
            #self.reset_context()

        except Exception as e:
            print(e)
            pass


    def unexcute(self):
        print(self)

    def load_page_list_to_ui(self):
        self.gui.tab1_page_listwidget.clear()
        for p in self.context.current_chapter.page_list:
            print(p)
            self.gui.tab1_page_listwidget.addItem(p.page_name)

    def get_selected_chapter(self,_selected_chapter):

        for c in self.context.current_book.chapter_list:
           print(c.chapter_name)
           if str(c.chapter_name) == str(_selected_chapter):
                return c
        return None




class SelectPageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            print(self)
            _selected_page=str(self.gui.tab1_page_listwidget.currentItem().text())
            print(_selected_page)
            _page = self.get_selected_page(_selected_page)
            print("page is",_page.page_name)
            self.context.current_page=_page
            assert _page is not None
            self.load_image_preview()

        except Exception as e:
            print(e)
            pass


    def unexcute(self):
        print(self)

    def get_selected_page(self, _selected_page):
        for p in self.context.current_chapter.page_list:
            print(p.page_name)
            if str(p.page_name) == str(_selected_page):
                return p
        return None

    def load_image_preview(self):
        _image_folder_path=self.context.current_page.page_file_path
        print(_image_folder_path)
        print(self.context.current_page.page_image_name)
        pixmap = QPixmap(_image_folder_path+"/"+self.context.current_page.page_image_name)
        self.gui.tab1_page_view.setPixmap(pixmap)



'''
buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')
 
'''