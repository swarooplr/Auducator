
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets

import controller.tab2_controller.commands as commands
import model.container
import controller.tab2_controller.commands.ResetUI as reset_ui
import controller.tab2_controller.commands.SelectLabelAudio as select_label


class AddNewLabelCommand(commands.BaseCommand):

    def __init__(self, context=None, gui=None):
        self.context=context
        self.gui=gui



    def execute(self):
        print(self)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.gui,"Select Image", "","All Files (*);;Image Files (*.png);;Image Files (*.jpeg);;Image Files (*.jpg)")
        fileName=self.context.current_page.page_file_path+"\\"+self.context.current_page.page_image_name
        print(fileName)
        if fileName:
            print(fileName)
            self.load_image_pop(fileName)


    def unexcute(self):
        print(self)


    def load_image_pop(self,filename):


        def onselect(eclick, erelease):
                if eclick.ydata>erelease.ydata:
                    eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
                if eclick.xdata>erelease.xdata:
                    eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
                #ax.set_ylim(erelease.ydata,eclick.ydata)                #ax.set_xlim(eclick.xdata,erelease.xdata)
                print (str(eclick.xdata)+" "+str(eclick.ydata))
                print (str(erelease.xdata)+" "+str(erelease.ydata))

                im = Image.open(filename)
                print(im.size)

                crop_rectangle = (eclick.xdata,eclick.ydata,erelease.xdata, erelease.ydata)
                cropped_im = im.crop(crop_rectangle)
                #cropped_im.show()
                cropped_im.save("cropped_image.png")
                pixmap = QPixmap('cropped_image.png')
                self.gui.tab2_label_preview.setPixmap(pixmap)
                print("cropped")
                fig.canvas.draw()

                _cropped_cordinates=(eclick.xdata,eclick.ydata,erelease.xdata,erelease.ydata)
                self.cropped_selected(_cropped_cordinates)
                return





        fig = plt.figure()
        fig.canvas.set_window_title('Select regions')
        ax = fig.add_subplot(111)
        im = Image.open(filename)
        arr = np.asarray(im)
        plt_image=plt.imshow(arr)
        rs=widgets.RectangleSelector(
                ax, onselect, drawtype='box',
                rectprops = dict(facecolor='red', edgecolor = 'black', alpha=0.5, fill=True))
        plt.show()



    def cropped_selected(self,_cropped_cordinates):


        self.context.current_label=None
        self.rest_ui=reset_ui.ResetUICommand(self.context,self.gui)
        self.rest_ui.execute()

        self.gui.tab2_label_listwidget.clear()
        for label in self.context.current_page.label_list:
            if(label.label_text is not None or
               not label.label_text == " "):
                self.gui.tab2_label_listwidget.addItem(label.label_text)
            else:
                self.gui.tab2_label_listwidget.addItem("Audio File")

        self.gui.tab2_label_listwidget.addItem("New_Label")

        new_label=model.container.Label("New Label"," ",None,None,False,False)
        new_label.set_coordinates(_cropped_cordinates[0],_cropped_cordinates[1],_cropped_cordinates[2],_cropped_cordinates[3])
        new_label.set_saved(False)
        self.context.current_label=new_label

        self.context.current_page.add_label(new_label)
        lastelement=len(self.context.current_page.label_list)-1
        self.gui.tab2_label_listwidget.setCurrentRow(lastelement)
        select_label.SelectLabelCommand(self.context,self.gui).execute()



