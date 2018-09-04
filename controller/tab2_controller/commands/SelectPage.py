import controller.tab2_controller.commands as commands
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.Inspectors as inspector
import controller.exceptions.ExceptionHandler as exceptionhandler
from PyQt5.QtGui import QIcon, QPixmap
import cv2
import imutils

class SelectPageCommand(commands.BaseCommand):
    """Command to execute after a page is selected,loads the corresponding label list into UI"""

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        try:
            print(self)
            _selected_page=str(self.gui.tab2_page_listwidget.currentItem().text())
            print(_selected_page)
            _page = self.get_selected_page(_selected_page)
            print("chapter",_page.page_name)
            self.context.current_page=_page
            assert _page is not None
            self.load_label_list_to_ui()

        except Exception as e:
            exceptionhandler.ExceptionHandler(e,self.gui).handle()
            pass


    def unexcute(self):
        print(self)

    def get_selected_page(self,_selected_page):
        """

        :param _selected_page: name of the page selected
        :type _selected_page:  string
        :return: corresponding page object
        :rtype:  Page
        """
        for p in self.context.current_chapter.page_list:
           print(p.page_name)
           if str(p.page_name) == str(_selected_page):
                return p
        return None

    @inspector.bookselected
    @inspector.chapterselected
    @inspector.pageselected
    def load_label_list_to_ui(self):
        """

        :return: loads the label list of page into UI
        :rtype: None
        """
        self.gui.tab2_label_listwidget.clear()

        img = cv2.imread(self.context.current_page.page_file_path+'/'+self.context.current_page.page_image_name)
        h = self.gui.tab2_page_preview.frameGeometry().height()
        w = self.gui.tab2_page_preview.frameGeometry().width()
        image = imutils.resize(img, height=h, width=w)
        cv2.imwrite("display.png",image)
        self.gui.tab2_page_preview.setPixmap(QPixmap("display.png"))

        for label in self.context.current_page.label_list:
            if(label.label_text is not None or
               not label.label_text == " "):
                self.gui.tab2_label_listwidget.addItem(label.label_text)
            else:
                self.gui.tab2_label_listwidget.addItem("Audio File")

    def reset_context(self):
      self.context.set_current_label(None)
      self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
      self.rest_ui.execute()
