# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseResolution.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_choose_resolution(object):
    def setupUi(self, choose_resolution):
        choose_resolution.setObjectName("choose_resolution")
        choose_resolution.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(choose_resolution)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(choose_resolution)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_3 = QtWidgets.QPushButton(choose_resolution)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(choose_resolution)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(choose_resolution)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(choose_resolution)
        QtCore.QMetaObject.connectSlotsByName(choose_resolution)

    def retranslateUi(self, choose_resolution):
        _translate = QtCore.QCoreApplication.translate
        choose_resolution.setWindowTitle(_translate("choose_resolution", "Dialog"))
        self.label.setText(_translate("choose_resolution", "Choose Resolution \nHeight X Width"))
        self.pushButton_3.setText(_translate("choose_resolution", "PushButton"))
        self.pushButton.setText(_translate("choose_resolution", "PushButton"))
        self.pushButton_2.setText(_translate("choose_resolution", "PushButton"))

