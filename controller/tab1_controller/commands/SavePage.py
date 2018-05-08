import controller.tab1_controller.commands as commands
import model as model
import os
import model.container.createContainer as createContainer

class SavePageCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        page_name = self.gui.tab1_page_name_input.text()
        print('page is :',page_name)

        page_name,page_file_path = createContainer.createPage(self.context.current_chapter.chapter_path,page_name)

        print("folder created :",page_name,page_file_path)

        page =  model.container.Page(page_name,page_file_path,[])
        self.context.current_chapter.add_page(page)
        self.gui.tab1_page_listwidget.addItem(page.page_name)


    def unexcute(self):
        print(self)