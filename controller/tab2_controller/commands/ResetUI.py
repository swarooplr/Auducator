import controller.tab2_controller.commands as commands
class ResetUICommand(commands.BaseCommand):
    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui

    def execute(self):
        print(self)
        try:

            if(self.context.current_book is None):
                self.gui.tab2_book_name_2.setText("Book Not Selected")
                self.gui.tab2_chapter_select_combobox.clear()

            if(self.context.current_chapter is None):
                self.gui.tab2_page_listwidget.clear()

            if(self.context.current_page is None):
                self.gui.tab2_label_listwidget.clear()

                #remove page preview

            if(self.context.current_label is None):
                self.gui.tab2_label_input.setText(" ")
                self.gui.tab2_description_input.setText(" ")
                self.gui.tab2_label_audio_file.setText(" ")
                self.gui.tab2_description_audio_file.setText(" ")
                #remove label preview
        except:
            pass
    def unexcute(self):
        pass
        self.rest_ui.execute()
