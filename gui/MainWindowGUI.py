# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auducatorv3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import gui.Tab1 as tab1
import gui.Tab2 as tab2
import gui.Tab3 as tab3

from controller.tab2_controller.commands import SelectBook,SelectLabelAudio,SelectPage,SelectChapter,DeleteElements,SaveLabel,AddNewLabel
from controller.tab3_controller.commands import SelectBook as SelectBook3,SelectChapter as SelectChapter3,PlayPage as PlayPage3
from controller.tab1_controller.commands import NewElements,SelectElements,SelectPicture,ManualCrop,TakePicture,SavePage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 850)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")


        tab1.Tab1Create().intiate(Ui_MainWindow)
        self.tabWidget.addTab(self.tab1, "")



        tab2.Tab2Create().intiate(Ui_MainWindow)
        self.tabWidget.addTab(self.tab2, "")

        tab3.Tab3Create().intiate(Ui_MainWindow)
        self.tabWidget.addTab(self.tab3, "")

        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.set_up_invoker()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)








    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auducator"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Select Pages"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Add Page Labels"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Play Book"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))


    def set_up_invoker(self):
         # tab1 invoker
         self.invoker_tab1.set_select_book_command(SelectElements.SelectBookCommand(self.invoker_tab1, self))
         self.invoker_tab1.set_select_chapter_command(SelectElements.SelectChapterCommand(self.invoker_tab1, self))
         self.invoker_tab1.set_select_page_command(SelectElements.SelectPageCommand(self.invoker_tab1, self))
         self.invoker_tab1.create_new_book_command(NewElements.NewBookCommand(self.invoker_tab1, self))
         self.invoker_tab1.create_new_chapter_command(NewElements.NewChapterCommand(self.invoker_tab1, self))
         # self.invoker_tab1.delete_book_command(DeleteElementsTab1.DeleteBookCommand(None, self))
         # self.invoker_tab1.delete_chapter_command(DeleteElementsTab1.DeletChapterCommand(None, self))
         # self.invoker_tab1.delete_page_command(DeleteElementsTab1.DeletPageCommand(None, self))
         self.invoker_tab1.manual_crop_command(ManualCrop.ManualCropCommand(self.invoker_tab1, self))
         self.invoker_tab1.save_page_command(SavePage.SavePageCommand(self.invoker_tab1, self))
         self.invoker_tab1.select_picture_command(SelectPicture.SelectPictureCommand(self.invoker_tab1, self))
         self.invoker_tab1.take_picture_command(TakePicture.TakePictureCommand(self.invoker_tab1, self))
         # self.invoker_tab1.rotate_image_command(RotatePage.RotatePa


         #tab2 invoker
         self.invoker_tab2.set_select_book_command(SelectBook.SelectBookCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_select_chapter_command(SelectChapter.SelectChapterCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_select_page_command(SelectPage.SelectPageCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_select_label_command(SelectLabelAudio.SelectLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_delete_page_command(DeleteElements.DeletePageCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_delete_label_command(DeleteElements.DeleteLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_select_audio_label_command(SelectLabelAudio.SelectAudioFileLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_select_audio_description_command(SelectLabelAudio.SelectAudioFileDescribeCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_save_label_command(SaveLabel.SaveLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_add_new_label_command(AddNewLabel.AddNewLabelCommand(self.invoker_tab2,self))


         #tab3 invoker
         self.invoker_tab3.set_select_book_command(SelectBook3.SelectBookCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_select_chapter_command(SelectChapter3.SelectChapterCommand(self.invoker_tab3,self))
         #self.invoker_tab3.set_select_page_command(SelectPage.SelectPageCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_play_page_command(PlayPage3.PlayPageCommand(self.invoker_tab3,self))










