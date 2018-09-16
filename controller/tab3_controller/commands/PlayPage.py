
import _thread
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab3_controller.commands as commands
import controller.tab3_controller.commands.ResetUI as reset_ui

import controller.tab3_controller.commands.speakout as speakout
import controller.Inspectors as inspector
import model.container.getContainer as getContainer
import controller.tab3_controller.commands.Tracker as tracker
import controller.exceptions.ExceptionHandler as exceptionhandler




class PlayPageCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        try:
            print(self)
            self.start_play()

        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass

    def unexcute(self):
        print(self)

    @inspector.bookselected
    @inspector.chapterselected
    def start_play(self):
            _selected_page=str(self.gui.tab3_page_listwidget.currentItem().text())
            print(_selected_page)
            _page = self.get_selected_page(_selected_page)
            print("page",_page.page_name)
            for i in _page.label_list:
                print("label",i.label_text)
            self.context.current_page=_page
            assert _page is not None

            tracker.cordinates = (0, 0)
            self.context.tracking_thread = threading.Thread(target=tracker.track,args=(self.context, self.gui))

            self.context.speakout_thread = threading.Thread(target=speakout.speakout,args=(_page.label_list,_page.page_file_path))

            #_thread.start_new_thread(track.trackit,("Thread-1",))
            #_thread.start_new_thread(speakout.speakout,(_page.label_list,_page.page_file_path))
            self.context.tracking_thread.start()
            self.context.speakout_thread.start()


    def get_selected_page(self,_selected_page):
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None

    def reset_context(self):
        pass

















