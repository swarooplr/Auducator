class Invoker:

    def __init__(self, gui, current_book=None, current_chapter=None):
        self.gui=gui
        self.current_book= current_book
        self.current_chapter= current_chapter


    def set_current_page(self, current_page):
       self.current_page = current_page

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


    def take_picture(self):
        self.take_picture_command.execute()

    def select_picture(self):
        self.select_picture_command.execute()

    def manual_crop(self):
        self.manual_crop_comand.execute()

    def rotate_image(self):
        self.rotate_image_command.execute()

    def save_page(self):
        self.save_page_command.execute()

