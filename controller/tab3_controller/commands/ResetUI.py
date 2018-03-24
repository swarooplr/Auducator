import controller.tab3_controller.commands as commands
class ResetUICommand(commands.BaseCommand):
    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui

    def execute(self):
        print(self)
        try:
            
            if(self.context.current_book is None):
                self.gui.tab3_book_display.setText("Book Not Selected")
                self.gui.tab3_select_chapter_combobox.clear()

            if(self.context.current_chapter is None):
                self.gui.tab3_page_listwidget.clear()

            if(self.context.current_page is None):
                pass
                #self.gui.tab3_label_listwidget.clear()

                #remove page preview

            
        except:
            pass
    def unexcute(self):
        pass
        self.rest_ui.execute()
