# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_colour.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_choose_colour(object):
    def setupUi(self, choose_colour,MainUI):
        choose_colour.setObjectName("choose_colour")
        choose_colour.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(choose_colour)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(choose_colour)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.pushButton = QtWidgets.QPushButton(choose_colour)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(choose_colour)
        QtCore.QMetaObject.connectSlotsByName(choose_colour)

    def retranslateUi(self, choose_colour):
        _translate = QtCore.QCoreApplication.translate
        choose_colour.setWindowTitle(_translate("choose_colour", "Choose Colour"))
        self.label.setText(_translate("choose_colour", "Click on the Tracking Colour"))
        self.pushButton.setText(_translate("choose_colour", "Green"))

