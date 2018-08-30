
import shutil
import json

import controller.tab2_controller.commands as commands
import controller.Inspectors as inspector
import controller.exceptions.ExceptionHandler as exceptionhandler


class SaveLabelCommand(commands.BaseCommand):
    """Command  saves the label once modifications are done"""

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui = gui



    def execute(self):
        try:
            self.identify_label()
        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass





    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    @inspector.labelselected
    def identify_label(self):
        """

        :return: returns selected label from listwidget
        :rtype:  Label
        """

        new_label_index=int(self.gui.tab2_label_listwidget.currentRow())
        new_label=self.context.current_page.label_list[new_label_index]

        label_text=str(self.gui.tab2_label_input.text())
        description_text=str(self.gui.tab2_description_input.toPlainText())
        _label_file=str(self.gui.tab2_label_audio_file.text())
        _description_file=str(self.gui.tab2_description_audio_file.text())

        print(label_text,description_text,_label_file,_description_file)
        self.context.current_page.label_list[new_label_index].set_label_text(label_text)
        self.context.current_page.label_list[new_label_index].set_description_text(description_text)

        project_directory=self.context.current_page.page_file_path
        print(project_directory)
        if(_label_file=="No File Selected" or _label_file==" " ):
            self.context.current_page.label_list[new_label_index].set_label_audio(_label_file)
            self.context.current_page.label_list[new_label_index].set_play_audio_label(False)
            pass
        else:
            shutil.copy(_label_file,project_directory)
            self.context.current_page.label_list[new_label_index].set_label_audio(_label_file.split('/')[-1])
            self.context.current_page.label_list[new_label_index].set_play_audio_label(True)
            pass

        if(_description_file=="No File Selected" or _description_file):
            self.context.current_page.label_list[new_label_index].set_description_audio(_description_file)
            self.context.current_page.label_list[new_label_index].set_play_audio_description(False)
            pass
        else:
            shutil.copy(_description_file,project_directory)
            self.context.current_page.label_list[new_label_index].set_description_audio(_description_file.split('/')[-1])
            self.context.current_page.label_list[new_label_index].set_play_audio_description(True)
            pass



        self.write_to_file(self.context.current_page.label_list[new_label_index])

    def write_to_file(self,label):
        """

        :param label: label to be saved
        :type label:  Label
        :return: None
        :rtype:
        """
        _config_file=open(str(self.context.current_page.page_file_path)+"/voice_over_details.json","r")
        _config=json.load(_config_file)
        _config_file.close()
        _config["label_list"].clear()

        for lab in self.context.current_page.label_list:
            _config["label_list"].append(lab.to_dict())

        print(_config)
        file=open(str(self.context.current_page.page_file_path)+"/voice_over_details.json","w")
        json.dump(_config,file)





"""
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
"""
