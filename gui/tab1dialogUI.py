# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab1dialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import controller.tab1_controller.Invoker as invoker
from controller.tab1_controller.commands import SelectPicture,ManualCrop,TakePicture,SavePage,RotatePage
import controller.supportingFunctions as sp

class Ui_Dialog(object):
    def setupUi(self, Dialog, MainUIRef):

        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(878, 781)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Page_view = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Page_view.setFont(font)
        self.Page_view.setAlignment(QtCore.Qt.AlignCenter)
        self.Page_view.setObjectName("Page_view")
        self.verticalLayout_3.addWidget(self.Page_view)
        self.page_rotate = QtWidgets.QPushButton(self.groupBox)
        self.page_rotate.setObjectName("page_rotate")
        self.verticalLayout_3.addWidget(self.page_rotate)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(240, 320))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.select_picture_2 = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_picture_2.sizePolicy().hasHeightForWidth())
        self.select_picture_2.setSizePolicy(sizePolicy)
        self.select_picture_2.setObjectName("select_picture_2")
        self.verticalLayout_5.addWidget(self.select_picture_2)
        self.take_picture = QtWidgets.QPushButton(self.groupBox_5)
        self.take_picture.setObjectName("take_picture")
        self.verticalLayout_5.addWidget(self.take_picture)
        self.spacer1 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer1.sizePolicy().hasHeightForWidth())
        self.spacer1.setSizePolicy(sizePolicy)
        self.spacer1.setText("")
        self.spacer1.setAlignment(QtCore.Qt.AlignCenter)
        self.spacer1.setObjectName("spacer1")
        self.verticalLayout_5.addWidget(self.spacer1)
        self.manual_crop_picture = QtWidgets.QPushButton(self.groupBox_5)
        self.manual_crop_picture.setObjectName("manual_crop_picture")
        self.verticalLayout_5.addWidget(self.manual_crop_picture)
        self.spacer2 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer2.sizePolicy().hasHeightForWidth())
        self.spacer2.setSizePolicy(sizePolicy)
        self.spacer2.setText("")
        self.spacer2.setAlignment(QtCore.Qt.AlignCenter)
        self.spacer2.setObjectName("spacer2")
        self.verticalLayout_5.addWidget(self.spacer2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.page_name_input = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_name_input.sizePolicy().hasHeightForWidth())
        self.page_name_input.setSizePolicy(sizePolicy)
        self.page_name_input.setObjectName("page_name_input")
        self.verticalLayout_5.addWidget(self.page_name_input)
        self.spacer3 = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer3.sizePolicy().hasHeightForWidth())
        self.spacer3.setSizePolicy(sizePolicy)
        self.spacer3.setText("")
        self.spacer3.setAlignment(QtCore.Qt.AlignCenter)
        self.spacer3.setObjectName("spacer3")
        self.verticalLayout_5.addWidget(self.spacer3)
        self.save_page = QtWidgets.QPushButton(self.groupBox_5)
        self.save_page.setObjectName("save_page")
        self.verticalLayout_5.addWidget(self.save_page)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.__set_up_click_events(MainUIRef)
        self.set_up_invoker(MainUIRef)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Page Creator"))
        self.groupBox.setTitle(_translate("Dialog", "Page Preview"))
        self.Page_view.setText(_translate("Dialog", "Page preview"))
        self.page_rotate.setText(_translate("Dialog", "Rotate"))
        self.groupBox_5.setTitle(_translate("Dialog", "Page Creation"))
        self.select_picture_2.setText(_translate("Dialog", "Select Picture"))
        self.take_picture.setText(_translate("Dialog", "Take Picture"))
        self.manual_crop_picture.setText(_translate("Dialog", "Manual Crop"))
        self.label_4.setText(_translate("Dialog", "Page Name : "))
        self.save_page.setText(_translate("Dialog", "Save"))


    def set_up_invoker(self,UI):

        self.invoker_tab1.manual_crop_command(ManualCrop.ManualCropCommand(self.invoker_tab1, UI.gui,self))
        self.invoker_tab1.save_page_command(SavePage.SavePageCommand(self.invoker_tab1, UI.gui,self))
        self.invoker_tab1.select_picture_command(SelectPicture.SelectPictureCommand(self.invoker_tab1, UI.gui,self))
        self.invoker_tab1.take_picture_command(TakePicture.TakePictureCommand(self.invoker_tab1, UI.gui,self))
        self.invoker_tab1.rotate_image_command(RotatePage.RotatePageCommand(self.invoker_tab1, UI.gui,self))

        print("invoker setup")

    def __set_up_click_events(Ui_MainWindow,UI):
        Ui_MainWindow.invoker_tab1 = invoker.Invoker(Ui_MainWindow, UI.context.current_book, UI.context.current_chapter, sp)

        Ui_MainWindow.take_picture.clicked.connect(Ui_MainWindow.invoker_tab1.take_picture)
        Ui_MainWindow.select_picture_2.clicked.connect(Ui_MainWindow.invoker_tab1.select_picture)
        Ui_MainWindow.manual_crop_picture.clicked.connect(Ui_MainWindow.invoker_tab1.manual_crop)
        Ui_MainWindow.page_rotate.clicked.connect(Ui_MainWindow.invoker_tab1.rotate_image)
        Ui_MainWindow.save_page.clicked.connect(Ui_MainWindow.invoker_tab1.save_page)

        print("click events setup")