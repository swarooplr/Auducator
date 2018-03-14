class Label:
    def __init__(self, label_text, description_text, label_audio, description_audio, play_audio_label,
                 play_audio_description, x1=0, x2=0, y1=0, y2=0):
        self.label_text = label_text
        self.description_text = description_text
        self.label_audio = label_audio
        self.description_audio = description_audio
        self.play_audio_label = play_audio_label
        self.play_audio_description = play_audio_description
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def set_coordinates(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def set_label_text(self, label_text):
        self.label_text = label_text

    def set_description_text(self, description_text):
        self.description_text = description_text

    def set_label_audio(self, label_audio):
        self.label_audio = label_audio

    def set_description_audio(self, description_audio):
        self.description_audio = description_audio

    def set_play_audio_label(self, status=True):
        self.play_audio_label = status

    def set_play_audio_description(self, status=True):
        self.play_audio_description = status


class Page:
    def __init__(self, page_name, label_list=[]):
        self.page_name= page_name
        self.label_list= label_list

    def set_label_list(self,label_list):
        self.label_list=label_list

    def add_label(self,label):
        self.label_list.append(label)

    def remove_label_at(self,index):
        self.label_list.remove(index)

    def remove_label(self,label):
        self.label_list.remove(label)


class Chapter:
    def __init__(self, chapter_name, page_list=[]):
        self.chapter_name= chapter_name
        self.page_list= page_list

    def set_page_list(self,page_list):
        self.page_list= page_list

    def add_page(self,page):
        self.page_list.append(page)

    def remove_page_at(self,index):
        self.page_list.remove(index)

    def remove_page(self,page):
        self.page_list.remove(page)

class Book:
    def __init__(self, book_name, chapter_list=[]):
        self.book_name= book_name
        self.chapter_list= chapter_list

    def set_chapter_list(self,chapter_list):
        self.chapter_list= chapter_list

    def add_chapter(self,chapter):
        self.chapter_list.append(chapter)

    def remove_chapter_at(self,index):
        self.chapter_list.remove(index)

    def remove_chapter(self,chapter):
        self.chapter_list.remove(chapter)



