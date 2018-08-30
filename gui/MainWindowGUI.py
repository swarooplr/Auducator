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

from controller.tab2_controller.commands import SelectBook,SelectLabelAudio,SelectPage,SelectChapter,DeleteElements,SaveLabel,AddNewLabel,NewElements
from controller.tab3_controller.commands import SelectBook as SelectBook3,SelectChapter as SelectChapter3,PlayPage as PlayPage3
#from controller.tab1_controller.commands import NewElements,SelectElements,SelectPicture,ManualCrop,TakePicture,SavePage


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

        #tab1.Tab1Create().intiate(Ui_MainWindow)
        #self.tabWidget.addTab(self.tab1, "")

        tab2.Tab2Create().intiate(Ui_MainWindow)
        self.tabWidget.addTab(self.tab2, "")

        tab3.Tab3Create().intiate(Ui_MainWindow)
        self.tabWidget.addTab(self.tab3, "")

        '''
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
        '''

        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
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
        self.actionChange_Color = QtWidgets.QAction(MainWindow)
        self.actionChange_Color.setObjectName("actionChange_Color")
        self.actionChange_picture_Size = QtWidgets.QAction(MainWindow)
        self.actionChange_picture_Size.setObjectName("actionChange_picture_Size")
        self.actionSet_Default_Path = QtWidgets.QAction(MainWindow)
        self.actionSet_Default_Path.setObjectName("actionSet_Default_Path")
        self.actionSet_Custom_Colour = QtWidgets.QAction(MainWindow)
        self.actionSet_Custom_Colour.setObjectName("actionSet_Custom_Colour")
        self.actionSet_Tracking_Rate = QtWidgets.QAction(MainWindow)
        self.actionSet_Tracking_Rate.setObjectName("actionSet_Tracking_Rate")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionFeedback = QtWidgets.QAction(MainWindow)
        self.actionFeedback.setObjectName("actionFeedback")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuSettings.addAction(self.actionChange_Color)
        self.menuSettings.addAction(self.actionChange_picture_Size)
        self.menuSettings.addAction(self.actionSet_Default_Path)
        self.menuSettings.addAction(self.actionSet_Custom_Colour)
        self.menuSettings.addAction(self.actionSet_Tracking_Rate)
        self.menuHelp.addAction(self.actionSearch)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuAbout.addAction(self.actionInfo)
        self.menuAbout.addAction(self.actionFeedback)
        self.menuAbout.addAction(self.actionCredits)
        self.menuAbout.addAction(self.actionContact)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.set_up_invoker()
        #self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auducator"))

        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Select Pages"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Add Page Labels"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Play Book"))

        #self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionChange_Color.setText(_translate("MainWindow", "Change Colour"))
        self.actionChange_picture_Size.setText(_translate("MainWindow", "Change picture Size"))
        self.actionSet_Default_Path.setText(_translate("MainWindow", "Set Default Path"))
        self.actionSet_Custom_Colour.setText(_translate("MainWindow", "Set Custom Colour"))
        self.actionSet_Tracking_Rate.setText(_translate("MainWindow", "Set Tracking Rate"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))

    def set_up_invoker(self):
         # tab1 invoker
         #self.invoker_tab1.set_select_book_command(SelectElements.SelectBookCommand(self.invoker_tab1, self))
         #self.invoker_tab1.set_select_chapter_command(SelectElements.SelectChapterCommand(self.invoker_tab1, self))
         #self.invoker_tab1.set_select_page_command(SelectElements.SelectPageCommand(self.invoker_tab1, self))
         #self.invoker_tab1.create_new_book_command(NewElements.NewBookCommand(self.invoker_tab1, self))
         #self.invoker_tab1.create_new_chapter_command(NewElements.NewChapterCommand(self.invoker_tab1, self))
         ## self.invoker_tab1.delete_book_command(DeleteElementsTab1.DeleteBookCommand(None, self))
         ## self.invoker_tab1.delete_chapter_command(DeleteElementsTab1.DeletChapterCommand(None, self))
         ## self.invoker_tab1.delete_page_command(DeleteElementsTab1.DeletPageCommand(None, self))
         #self.invoker_tab1.manual_crop_command(ManualCrop.ManualCropCommand(self.invoker_tab1, self))
         #self.invoker_tab1.save_page_command(SavePage.SavePageCommand(self.invoker_tab1, self))
         #self.invoker_tab1.select_picture_command(SelectPicture.SelectPictureCommand(self.invoker_tab1, self))
         #self.invoker_tab1.take_picture_command(TakePicture.TakePictureCommand(self.invoker_tab1, self))
         # self.invoker_tab1.rotate_image_command(RotatePage.RotatePa


         #tab2 invoker
         self.invoker_tab2.create_new_book_command(NewElements.NewBookCommand(self.invoker_tab2, self))
         self.invoker_tab2.create_new_chapter_command(NewElements.NewChapterCommand(self.invoker_tab2, self))
         self.invoker_tab2.delete_book_command(DeleteElements.DeleteBookCommand(self.invoker_tab2, self))
         self.invoker_tab2.delete_chapter_command(DeleteElements.DeleteChapterCommand(self.invoker_tab2, self))
         self.invoker_tab2.new_page_command(NewElements.NewPageCommand(self.invoker_tab2, self))

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










