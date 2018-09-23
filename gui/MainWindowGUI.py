# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auducatorv3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog

import gui.Tab1 as tab1
import gui.Tab2 as tab2
import gui.Tab3 as tab3

from controller.tab2_controller.commands import SelectBook,SelectLabelAudio,SelectPage,SelectChapter,DeleteElements,SaveLabel,AddNewLabel,NewElements,RecordingAudio
from controller.tab3_controller.commands import SelectBook as SelectBook3,SelectChapter as SelectChapter3,PlayPage as PlayPage3, StopPage as StopPage3, SelectPage as SelectPage3
from controller.menu_bar.settings import ChooseColour,InvertCamera,CustomColour,DefaultPath,PictureSize,TrackingRate,TestTracking,ChooseCamera,TestPageDetection
from controller.menu_bar import Invoker as invoker
from functools import partial
from gui.menu_bar import help
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

        self.actionChange_Camera = QtWidgets.QAction(MainWindow)
        self.actionChange_Camera.setObjectName("actionChange_camera")

        self.actionTestPageDetection = QtWidgets.QAction(MainWindow)
        self.actionTestPageDetection.setObjectName("actionPageDetection")

        self.actionTestTracking = QtWidgets.QAction(MainWindow)
        self.actionTestTracking.setObjectName("actionTestTracking")

        self.actionInvertCamera = QtWidgets.QAction(MainWindow)
        self.actionInvertCamera.setObjectName("InvertCamera")

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
        self.menuSettings.addAction(self.actionChange_Camera)
        self.menuSettings.addAction(self.actionTestPageDetection)
        self.menuSettings.addAction(self.actionTestTracking)
        self.menuSettings.addAction(self.actionInvertCamera)
        #self.menuHelp.addAction(self.actionSearch)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuAbout.addAction(self.actionInfo)
        #self.menuAbout.addAction(self.actionFeedback)
        self.menuAbout.addAction(self.actionCredits)
        self.menuAbout.addAction(self.actionContact)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        self.set_up_settings_click()
        self.set_up_help()
        self.set_up_invoker()
        #self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TALK"))

        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Select Pages"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Add Page Labels"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Play Book"))

        #self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionChange_Color.setText(_translate("MainWindow", "Change Colour"))

        self.actionChange_Camera.setText(_translate("MainWindow","Choose Camera"))
        self.actionTestPageDetection.setText(_translate("MainWindow","Test Page Detection"))
        self.actionTestTracking.setText(_translate("MainWindow","Test Tracking"))

        self.actionChange_picture_Size.setText(_translate("MainWindow", "Change picture Size"))
        self.actionSet_Default_Path.setText(_translate("MainWindow", "Set Default Path"))
        self.actionSet_Custom_Colour.setText(_translate("MainWindow", "Set Custom Colour"))
        self.actionSet_Tracking_Rate.setText(_translate("MainWindow", "Set Tracking Rate"))
        self.actionInvertCamera.setText(_translate("MainWindow","Invert Camera"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionFeedback.setText(_translate("MainWindow", "Feedback"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))


    def set_up_settings_click(self):
        self.invoker_settings = invoker.Invoker(self)

        self.actionChange_Color.triggered.connect(self.invoker_settings.choose_color)
        self.actionChange_picture_Size.triggered.connect(self.invoker_settings.picture_size)
        self.actionSet_Custom_Colour.triggered.connect(self.invoker_settings.custom_colour)
        self.actionSet_Default_Path.triggered.connect(self.invoker_settings.default_path)
        self.actionSet_Tracking_Rate.triggered.connect(self.invoker_settings.tracking_rate)
        self.actionChange_Camera.triggered.connect(self.invoker_settings.choose_camera)
        self.actionTestPageDetection.triggered.connect(self.invoker_settings.test_page_detection)
        self.actionTestTracking.triggered.connect(self.invoker_settings.test_tracking)
        self.actionInvertCamera.triggered.connect(self.invoker_settings.invert_camera)

    def set_up_help(self):
        self.actionCredits.triggered.connect(partial(self.show_help,"credits.txt"))
        self.actionHow_to_use.triggered.connect(partial(self.show_help, "how_to_use.txt"))
        self.actionContact.triggered.connect(partial(self.show_help, "contact.txt"))
        self.actionInfo.triggered.connect(partial(self.show_help, "info.txt"))

    def set_up_invoker(self):

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
         self.invoker_tab2.set_select_audio_description_command(SelectLabelAudio.SelectAudioFileLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_save_label_command(SaveLabel.SaveLabelCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_add_new_label_command(AddNewLabel.AddNewLabelCommand(self.invoker_tab2,self))

         self.invoker_tab2.set_start_recording_command(RecordingAudio.StartRecordingCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_stop_recording_command(RecordingAudio.StopRecordingCommand(self.invoker_tab2,self))
         self.invoker_tab2.set_play_recording_command(RecordingAudio.PlayRecordingCommand(self.invoker_tab2,self))

         #tab3 invoker
         self.invoker_tab3.set_select_book_command(SelectBook3.SelectBookCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_select_chapter_command(SelectChapter3.SelectChapterCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_stop_page_command(StopPage3.StopPageCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_play_page_command(PlayPage3.PlayPageCommand(self.invoker_tab3,self))
         self.invoker_tab3.set_select_page_command(SelectPage3.SelectPageCommand(self.invoker_tab3,self))


         #menu_bar invoker
         self.invoker_settings.set_choose_colour_setting(ChooseColour.ChooseColourSetting(self.invoker_settings,self))
         self.invoker_settings.set_picture_size_setting(PictureSize.PictureSizeSetting(self.invoker_settings, self))
         self.invoker_settings.set_default_path_setting(DefaultPath.DefaultPathSetting(self.invoker_settings, self))
         self.invoker_settings.set_tracking_rate_setting(TrackingRate.TrackingRateSetting(self.invoker_settings, self))
         self.invoker_settings.set_custom_colour_setting(CustomColour.CustomColourSetting(self.invoker_settings, self))
         self.invoker_settings.set_choose_camera_setting(ChooseCamera.ChooseCameraSetting(self.invoker_settings,self))
         self.invoker_settings.set_test_page_detection_setting(TestPageDetection.TestPageDetectionSetting(self.invoker_settings,self))
         self.invoker_settings.set_test_tracking_setting(TestTracking.TestTrackingSetting(self.invoker_settings,self))
         self.invoker_settings.set_invert_camera_setting(InvertCamera.InvertCameraSetting(self.invoker_settings,self))

    def show_help(self,type):

        class AppWindow(QDialog):
            def __init__(self, content,title):
                print(content)
                super().__init__()
                self.ui = help.Ui_Help()
                self.ui.setupUi(self)
                self.ui.plainTextEdit.setPlainText(content)
                self.setWindowTitle(title)
        content = open(type, "r").read()
        self.w = AppWindow(content,type.split(".")[0])
        self.w.setModal(True)
        self.w.show()










