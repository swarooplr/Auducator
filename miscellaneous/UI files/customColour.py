# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customColour.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_customColour(object):
    def setupUi(self, customColour):
        customColour.setObjectName("customColour")
        customColour.resize(590, 273)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(customColour)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(customColour)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pl1 = QtWidgets.QLineEdit(customColour)
        self.pl1.setObjectName("pl1")
        self.horizontalLayout_3.addWidget(self.pl1)
        self.pl2 = QtWidgets.QLineEdit(customColour)
        self.pl2.setObjectName("pl2")
        self.horizontalLayout_3.addWidget(self.pl2)
        self.pl3 = QtWidgets.QLineEdit(customColour)
        self.pl3.setObjectName("pl3")
        self.horizontalLayout_3.addWidget(self.pl3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(customColour)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pu1 = QtWidgets.QLineEdit(customColour)
        self.pu1.setObjectName("pu1")
        self.horizontalLayout_5.addWidget(self.pu1)
        self.pu2 = QtWidgets.QLineEdit(customColour)
        self.pu2.setObjectName("pu2")
        self.horizontalLayout_5.addWidget(self.pu2)
        self.pu3 = QtWidgets.QLineEdit(customColour)
        self.pu3.setObjectName("pu3")
        self.horizontalLayout_5.addWidget(self.pu3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(customColour)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(customColour)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(customColour)
        QtCore.QMetaObject.connectSlotsByName(customColour)

    def retranslateUi(self, customColour):
        _translate = QtCore.QCoreApplication.translate
        customColour.setWindowTitle(_translate("customColour", "Custom Colour"))
        self.label_8.setText(_translate("customColour", "Lower Limit"))
        self.label_9.setText(_translate("customColour", "Upper Limit"))
        self.pushButton_2.setText(_translate("customColour", "C1"))
        self.pushButton_3.setText(_translate("customColour", "C2"))

