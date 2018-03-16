import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
class SaveLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        print("========")
        print("book",self.context.current_book.book_folder_path)
        for i in self.context.current_book.chapter_list:
            print(i.chapter_name)
        print("chapter",self.context.current_chapter.chapter_name)
        for i in self.context.current_chapter.page_list:
            print(i.page_name)
        print("page",self.context.current_page.page_name)
        for i in self.context.current_page.label_list:
            print(i.label_text)
        print("label",self.context.current_label.label_text)




    def unexcute(self):
        print(self)



