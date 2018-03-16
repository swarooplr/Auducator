import controller.tab2_controller.commands as commands
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.Inspectors as inspector

class SelectPageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            print(self)
            _selected_page=str(self.gui.tab2_page_listwidget.currentItem().text())
            print(_selected_page)
            _page = self.get_selected_page(_selected_page)
            print("chapter",_page.page_name)
            self.context.current_page=_page
            assert _page is not None
            self.load_label_list_to_ui()

        except Exception as e:
            print(e)
            pass


    def unexcute(self):
        print(self)

    def get_selected_page(self,_selected_page):
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    def load_label_list_to_ui(self):
        self.gui.tab2_label_listwidget.clear()
        for label in self.context.current_page.label_list:
            if(label.label_text is not None or
               not label.label_text == " "):
                self.gui.tab2_label_listwidget.addItem(label.label_text)
            else:
                self.gui.tab2_label_listwidget.addItem("Audio File")

    def reset_context(self):
      self.context.set_current_label(None)
      self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
      self.rest_ui.execute()
