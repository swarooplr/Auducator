import controller.tab2_controller.commands as commands
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.Inspectors as inspector
class SelectChapterCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        try:
            print(self)
            #self.gui.tab2_page_listwidget.clear()
            _selected_chapter=str(self.gui.tab2_chapter_select_combobox.currentText())
            print("_selected chapter",_selected_chapter)
            _chapter=self.get_selected_chapter(_selected_chapter)
            print("chapter returned",len(_chapter.page_list))
            self.context.current_chapter=_chapter
            #assert _chapter is not None
            self.load_page_list_to_ui()
            self.reset_context()

        except Exception as e:
            print(e)
            pass



    def unexcute(self):
        print(self)


    def get_selected_chapter(self,_selected_chapter):

        for c in self.context.current_book.chapter_list:
           print(c.chapter_name)
           if str(c.chapter_name) == str(_selected_chapter):
                return c
        return None

    @inspector.bookselected
    @inspector.chapterselected
    def load_page_list_to_ui(self):
        self.gui.tab2_page_listwidget.clear()
        for p in self.context.current_chapter.page_list:
            self.gui.tab2_page_listwidget.addItem(p.page_name)

    def reset_context(self):
        self.context.set_current_page(None)
        self.context.set_current_label(None)
        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()
