import json
import shutil


import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.exceptions.ExceptionHandler as exceptionhandler

class DeletePageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui

    def execute(self):
        print(self)
        try:
            self.delete_page()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass



    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    def delete_page(self):

        #alert

        _selected_page=str(self.gui.tab2_page_listwidget.currentItem().text())
        print("to delete ",_selected_page)
        _page=self.get_selected_page(_selected_page)
        assert not _page is  None

        #delete from current context
        self.context.current_chapter.remove_page(_page)


        #delete folder from database
        shutil.rmtree(_page.page_file_path)

        #set current page context null
        #call resetui method
        self.gui.tab2_page_listwidget.clear()
        for p in self.context.current_chapter.page_list:
            print(p)
            self.gui.tab2_page_listwidget.addItem(p.page_name)
        self.reset_context()


    def get_selected_page(self,_selected_page):
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None

    def reset_context(self):
        self.context.set_current_page(None)
        self.context.set_current_label(None)
        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()




class DeleteLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            self.delete_label()
        except Exception as e:
            print(e)
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass

    def unexcute(self):
        print(self)


    @inspector.labelselected
    def delete_label(self):
        #alert
        _selected_label_index=str(self.gui.tab2_label_listwidget.currentRow())
        #delete from file
        _label=self.get_selected_label(_selected_label_index)
        print(_label.label_text)
        assert not _label is  None

        #remove from context
        self.context.current_page.remove_label(_label)

        #delete element from listwidget (reload)
        self.gui.tab2_label_listwidget.clear()
        for label in self.context.current_page.label_list:
            if(label.label_text is not None or
               not label.label_text == " "):
                self.gui.tab2_label_listwidget.addItem(label.label_text)
            else:
                self.gui.tab2_label_listwidget.addItem("Audio File")


        #change json file in folder
        self.update_json(_selected_label_index)
        #set current  label  in context null

        #call resetcontext method
        self.reset_context()



    def get_selected_label(self,_selected_label_index):
        """

        :param _selected_label_index: index of selected label from listwidget
        :type _selected_label_index: int
        :return: corresponding label object
        :rtype: Label
        """
        if len(self.context.current_page.label_list) <= int(_selected_label_index):
            return None
        else:
            return self.context.current_page.label_list[int(_selected_label_index)]


    def update_json(self,_selected_label_index):
        _config_file=open(str(self.context.current_page.page_file_path)+"/voice_over_details.json","r")
        _config=json.load(_config_file)
        _config_file.close()
        _config["label_list"].pop((int)(_selected_label_index))
        print(_config["label_list"])
        file=open(str(self.context.current_page.page_file_path)+"/voice_over_details.json","w")
        json.dump(_config,file)


    def reset_context(self):
        self.context.set_current_label(None)
        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()





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
