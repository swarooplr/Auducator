import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
class DeletePageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui

    def execute(self):
        print(self)
        try:
            self.delete_page()
        except:
            pass


    def unexcute(self):
        print(self)

    @inspector.pageselected
    def delete_page(self):
        #alert
        _selected_page=self.gui.self.tab2_page_listwidget.currentItem().text()
        #delete from file
        _page=self.get_selected_page(_selected_page)
        assert not _page is  None

        #delete element from listwidget
        #delete element from current chapter
        #delete folder from database
        #set current page context null
        #call resetui method


    def get_selected_page(self,_selected_page):
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None




class DeleteLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)


    def unexcute(self):
        print(self)


    @inspector.labelselected
    def delete_label(self):
        #alert
        _selected_label=self.gui.self.tab2_label_listwidget.currentItem().text()
        #delete from file
        _page=self.get_selected_page(_selected_label)
        assert not _page is  None

        #delete element from listwidget
        #delete element from current page
        #change json file in folder
        #set current  label  in context null
        #call resetui method


    def get_selected_page(self,_selected_page):
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None



class DeleteBookCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)

    def unexcute(self):
        print(self)

class DeleteChapterCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)

    def unexcute(self):
        print(self)
