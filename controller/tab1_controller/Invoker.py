class Invoker:

    def __init__(self, gui, current_book=None, current_chapter=None, current_page=None):
        self.gui=gui
        self.current_book= current_book
        self.current_chapter= current_chapter
        self.current_page= current_page

    def set_current_book(self, current_book):
        self.current_book = current_book

    def set_current_chapter(self, current_chapter):
       self.current_chapter = current_chapter

    def set_current_page(self, current_page):
       self.current_page = current_page

    def set_select_book_command(self, select_book_command):
        self.select_book_command = select_book_command

    def set_select_chapter_command(self,select_chapter_command):
        self.select_chapter_command=select_chapter_command

    def set_select_page_command(self, select_page_command):
        self.select_page_command = select_page_command

    def create_new_book_command(self,new_book_command):
        self.new_book_command = new_book_command

    def create_new_chapter_command(self,new_chapter_command):
        self.new_chapter_command = new_chapter_command

    def delete_book_command(self,delete_book_command):
        self.delete_book_command = delete_book_command

    def delete_chapter_command(self, delete_chapter_command):
        self.delete_chapter_command = delete_chapter_command

    def delete_page_command(self, delete_page_command):
        self.delete_page_command = delete_page_command

    def manual_crop_command(self,manual_crop_command):
        self.manual_crop_comand = manual_crop_command

    def save_page_command(self,save_page_command):
        self.save_page_command = save_page_command

    def select_picture_command(self,select_picture_command):
        self.select_picture_command = select_picture_command

    def take_picture_command(self,take_picture_command):
        self.take_picture_command = take_picture_command

    def rotate_image_command(self,rotate_image_command):
        self.rotate_image_command = rotate_image_command

    def select_book(self):
        self.select_book_command.execute()

    def select_chapter(self):
        self.select_chapter_command.execute()

    def select_page(self):
        self.select_page_command.execute()

    def new_book(self):
        self.new_book_command.execute()

    def new_chapter(self):
        self.new_chapter_command.execute()

    def delete_book(self):
        self.delete_book_command.execute()

    def delete_chapter(self):
        self.delete_chapter_command.execute()

    def take_picture(self):
        self.take_picture_command.execute()

    def select_picture(self):
        self.select_picture_command.execute()

    def manual_crop(self):
        self.manual_crop_comand.execute()

    def rotate_image(self):
        self.rotate_image_command.execute()

    def delete_page(self):
        self.delete_page_command.execute()

    def save_page(self):
        self.save_page_command.execute()

