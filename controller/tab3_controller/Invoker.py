

class Invoker:

    def __init__(self, gui, current_book=None, current_chapter=None, current_page=None):
        self.gui=gui
        self.current_book= current_book
        self.current_chapter= current_chapter
        self.current_page= current_page


    def set_current_book(self,current_book):
        self.current_book=current_book

    def set_current_chapter(self,current_chapter):
        self.current_chapter=current_chapter

    def set_current_page(self,current_page):
        self.current_page=current_page



    def set_select_book_command(self,select_book_command):
        self.select_book_command=select_book_command

    def set_select_chapter_command(self,select_chapter_command):
        self.select_chapter_command=select_chapter_command

    def set_select_page_command(self,select_page_command):
        self.select_page_command=select_page_command

    def set_play_page_command(self,select_play_page_command):
        self.play_page_command=select_play_page_command

    def set_stop_page_command(self,select_stop_page_command):
        self.stop_page_command=select_stop_page_command

    def select_book(self):
        print("connected")
        self.select_book_command.execute()


    def select_chapter(self):
        print("connected")
        self.select_chapter_command.execute()

    def select_page(self):
        print("connected")
        self.select_page_command.execute()

    def play_page(self):
        self.play_page_command.execute()

    def set_ui_(self,gui):
        self.gui=gui

    def stop_page(self):
        print("connected")
        self.stop_page_command.execute()





