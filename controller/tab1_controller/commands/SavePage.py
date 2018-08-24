import controller.tab1_controller.commands as commands
import model as model
import os
from PyQt5.QtGui import QIcon, QPixmap
import model.container.createContainer as createContainer
import model.container.getContainer as getContainer

class SavePageCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None, dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        print(self)
        page_name = self.dialog.page_name_input.text()
        print('page is :',page_name)

        page_file_path = createContainer.createPage(self.context.current_chapter.chapter_path,page_name)

        print("folder created :",page_name,page_file_path)

        page = getContainer.loadPage(page_name,page_file_path)

        self.context.current_chapter.add_page(page)

        self.gui.tab2_page_listwidget.addItem(page.page_name)

        self.dialog.Dialog.close()



    def unexcute(self):
        print(self)