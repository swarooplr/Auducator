import os
import cv2
import json

import model.container

def createBook(book_folder_path):
    os.makedirs(book_folder_path)
    config_path = os.path.join(book_folder_path,'Config')
    #metaData_path = os.path.join(book_folder_path,"MetaData")
    os.makedirs(config_path)
    #os.makedirs(metaData_path)
    os.makedirs(os.path.join(config_path,'Default'))

    _book = model.container.Book(book_folder_path, [])

    return _book


def createPage(chapter_path,page_name):

    voice_over_details = dict()

    page_path = chapter_path + '/' + page_name
    os.makedirs(page_path)

    img = cv2.imread('selectedImage.png')
    cv2.imwrite(page_path+'/'+page_name + '.png', img)


    voice_over_details["imagename"] = page_name+'.png'

    voice_over_details["label_list"] = list()

    voice_over_details["imageheight"] = 800

    voice_over_details["imagewidth"] = 600

    data = json.dumps(voice_over_details)
    with open(page_path+"/voice_over_details.json", "w") as f:
        f.write(data)

    return page_path