import os
import json
import shutil


import model.container

def loadBook(book_folder_path):
    try:
        _subfolders = [(f.name,f.path) for f in os.scandir(book_folder_path) if f.is_dir() ]
        _book=model.container.Book(book_folder_path)
        for f in _subfolders:
            try:
                _book.add_chapter(loadChapter(f[0],f[1]))
            except:
                pass
    except:
        pass
    pass


def loadChapter(chapter_name,chapter_folder_path):
    try:
        print(chapter_name,chapter_folder_path)
        _chapter = model.container.Chapter(chapter_name,chapter_folder_path)
        _subfolders = [(f.name,f.path) for f in os.scandir(chapter_folder_path) if f.is_dir() ]
        for f in _subfolders:
            try:
                _chapter.add_page(loadPage(f[0],f[1]))
            except:
                pass

        return _chapter
    except:
        pass
    pass


def loadPage(page_name,page_folder_path):
    try:
        print(page_name,page_folder_path)
        _page=model.container.Page(page_name,page_folder_path)
        _config_file=open(str(page_folder_path)+"/config.txt","r")
        _config=json.load(_config_file)
        _config_file.close()
        print(_config)
        for label_itr in _config["label_list"]:
            try:
              label=model.container.Label(label_itr["label_text"],label_itr["description_text"],label_itr["label_audio"],label_itr["description_audio"],label_itr["play_audio_labe"],label_itr["play_audio_description"],label_itr["x1"],label_itr["x2"],label_itr["y1"],label_itr["y2"])
              _page.add_label(label)
            except:pass

        return _page
    except:
        pass
    pass

