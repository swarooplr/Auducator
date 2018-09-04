

class Invoker:
    """
    sets the commands to be called when a event occurs
    maintains the context
    """
    def __init__(self, gui, current_book=None, current_chapter=None, current_page=None,current_label=None):
        self.gui=gui
        self.current_book= current_book
        self.current_chapter= current_chapter
        self.current_page= current_page
        self.current_label=current_label

    def set_current_book(self,current_book):
        self.current_book=current_book

    def set_current_chapter(self,current_chapter):
        self.current_chapter=current_chapter

    def set_current_page(self,current_page):
        self.current_page=current_page

    def set_current_label(self,current_label):
        self.current_label=current_label

    def set_select_book_command(self,select_book_command):
        self.select_book_command=select_book_command

    def set_select_chapter_command(self,select_chapter_command):
        self.select_chapter_command=select_chapter_command

    def set_select_page_command(self,select_page_command):
        self.select_page_command=select_page_command

    def set_select_label_command(self,select_label_command):
        self.select_label_command=select_label_command

    def set_save_label_command(self,save_label_command):
        self.save_label_command=save_label_command

    def set_delete_label_command(self,delete_label_command):
        self.delete_label_command=delete_label_command

    def set_delete_page_command(self,delete_page_command):
        self.delete_page_command=delete_page_command

    def set_select_audio_label_command(self,select_audio_label):
        self.select_audio_label_command=select_audio_label

    def set_select_audio_description_command(self,select_audio_description):
        self.select_audio_desciption_command=select_audio_description

    def set_add_new_label_command(self,add_new_label):
        self.add_new_label_command=add_new_label

    def select_book(self):
        print("connected")
        self.select_book_command.execute()


    def select_chapter(self):
        print("connected")
        self.select_chapter_command.execute()

    def select_page(self):
        print("connected")
        self.select_page_command.execute()

    def select_label(self):
        print("connected")
        self.select_label_command.execute()

    def add_new_label(self):
        print("connected")
        self.add_new_label_command.execute()


    def save_label(self):
        print("connected")
        self.save_label_command.execute()


    def delete_label(self):
        print("connected ")
        self.delete_label_command.execute()

    def delete_page(self):
        print("connected")
        self.delete_page_command.execute()

    def select_audio_label(self):
        print("connected")
        self.select_audio_label_command.execute()

    def select_audio_description(self):
        print("connected")
        self.select_audio_desciption_command.execute()

    def set_ui_(self,gui):
        self.gui=gui


    ## From tab one 5 actions
    def create_new_book_command(self, new_book_command):
        self.new_book_command = new_book_command

    def create_new_chapter_command(self, new_chapter_command):
        self.new_chapter_command = new_chapter_command

    def delete_book_command(self, delete_book_command):
        self.delete_book_command = delete_book_command

    def delete_chapter_command(self, delete_chapter_command):
        self.delete_chapter_command = delete_chapter_command

    def new_page_command(self, new_page_command):
        self.new_page_command = new_page_command


    def new_book(self):
        self.new_book_command.execute()

    def new_chapter(self):
        self.new_chapter_command.execute()

    def delete_book(self):
        self.delete_book_command.execute()

    def delete_chapter(self):
        self.delete_chapter_command.execute()

    def new_page(self):
        self.new_page_command.execute()

    #recording features

    def set_start_recording_command(self,start_recording_command):
        self.start_recording_command = start_recording_command

    def start_recording(self):
        print("connected")
        self.start_recording_command.execute()

    def set_stop_recording_command(self,stop_recording_command):
        self.stop_recording_command = stop_recording_command

    def stop_recording(self):
        print("connected")
        self.stop_recording_command.execute()

    def set_play_recording_command(self,play_recording_command):
        self.play_recording_command = play_recording_command

    def play_recording(self):
        print("connected")
        self.play_recording_command.execute()


