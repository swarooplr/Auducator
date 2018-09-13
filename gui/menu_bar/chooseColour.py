# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseColour.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_choose_colour(object):
    def setupUi(self, choose_colour):
        choose_colour.setObjectName("choose_colour")
        choose_colour.resize(297, 342)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(choose_colour)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChooseColour = QtWidgets.QLabel(choose_colour)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChooseColour.sizePolicy().hasHeightForWidth())
        self.ChooseColour.setSizePolicy(sizePolicy)
        self.ChooseColour.setObjectName("ChooseColour")
        self.verticalLayout.addWidget(self.ChooseColour)
        self.pushButton = QtWidgets.QPushButton(choose_colour)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(choose_colour)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(choose_colour)
        QtCore.QMetaObject.connectSlotsByName(choose_colour)

    def retranslateUi(self, choose_colour):
        _translate = QtCore.QCoreApplication.translate
        choose_colour.setWindowTitle(_translate("choose_colour", "Dialog"))
        self.ChooseColour.setText(_translate("choose_colour", "Choose Colour"))
        self.pushButton.setText(_translate("choose_colour", "C1"))
        self.pushButton_2.setText(_translate("choose_colour", "C2"))

