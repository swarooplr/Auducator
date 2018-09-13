

from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab3_controller.Invoker as invoker
class Tab3Create:

    def intiate(self,Ui_MainWindow):
        
        Ui_MainWindow.tab3 = QtWidgets.QWidget()
        Ui_MainWindow.tab3.setObjectName("tab3")
        Ui_MainWindow.verticalLayout_16 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab3)
        Ui_MainWindow.verticalLayout_16.setObjectName("verticalLayout_16")
        Ui_MainWindow.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_17.setObjectName("horizontalLayout_17")
        Ui_MainWindow.tab3_groupBox_6 = QtWidgets.QGroupBox(Ui_MainWindow.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_groupBox_6.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_groupBox_6.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_groupBox_6.setBaseSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainWindow.tab3_groupBox_6.setFont(font)
        Ui_MainWindow.tab3_groupBox_6.setObjectName("tab3_groupBox_6")
        Ui_MainWindow.horizontalLayout_18 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab3_groupBox_6)
        Ui_MainWindow.horizontalLayout_18.setObjectName("horizontalLayout_18")
        Ui_MainWindow.tab3_book_display = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_6)
        Ui_MainWindow.tab3_book_display.setObjectName("tab3_book_display")
        Ui_MainWindow.horizontalLayout_18.addWidget(Ui_MainWindow.tab3_book_display)
        Ui_MainWindow.tab3_select_book = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_select_book.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_select_book.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_select_book.setObjectName("tab3_select_book")
        Ui_MainWindow.horizontalLayout_18.addWidget(Ui_MainWindow.tab3_select_book)
        Ui_MainWindow.horizontalLayout_17.addWidget(Ui_MainWindow.tab3_groupBox_6)
        Ui_MainWindow.tab3_groupBox_7 = QtWidgets.QGroupBox(Ui_MainWindow.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_groupBox_7.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_groupBox_7.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_groupBox_7.setBaseSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainWindow.tab3_groupBox_7.setFont(font)
        Ui_MainWindow.tab3_groupBox_7.setObjectName("tab3_groupBox_7")
        Ui_MainWindow.horizontalLayout_19 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab3_groupBox_7)
        Ui_MainWindow.horizontalLayout_19.setObjectName("horizontalLayout_19")
        Ui_MainWindow.tab3_chapter_label = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_7)
        Ui_MainWindow.tab3_chapter_label.setObjectName("tab3_chapter_label")
        Ui_MainWindow.horizontalLayout_19.addWidget(Ui_MainWindow.tab3_chapter_label)
        Ui_MainWindow.tab3_select_chapter_combobox = QtWidgets.QComboBox(Ui_MainWindow.tab3_groupBox_7)
        Ui_MainWindow.tab3_select_chapter_combobox.setObjectName("tab3_select_chapter_combobox")
        Ui_MainWindow.horizontalLayout_19.addWidget(Ui_MainWindow.tab3_select_chapter_combobox)
        Ui_MainWindow.horizontalLayout_17.addWidget(Ui_MainWindow.tab3_groupBox_7)
        Ui_MainWindow.verticalLayout_16.addLayout(Ui_MainWindow.horizontalLayout_17)
        Ui_MainWindow.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_20.setObjectName("horizontalLayout_20")
        Ui_MainWindow.tab3_groupBox_8 = QtWidgets.QGroupBox(Ui_MainWindow.tab3)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab3_groupBox_8.setFont(font)
        Ui_MainWindow.tab3_groupBox_8.setObjectName("tab3_groupBox_8")
        Ui_MainWindow.verticalLayout_12 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab3_groupBox_8)
        Ui_MainWindow.verticalLayout_12.setObjectName("verticalLayout_12")
        Ui_MainWindow.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_22.setObjectName("horizontalLayout_22")
        Ui_MainWindow.tab3_page_listwidget = QtWidgets.QListWidget(Ui_MainWindow.tab3_groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_page_listwidget.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_page_listwidget.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_page_listwidget.setObjectName("tab3_page_listwidget")
        Ui_MainWindow.horizontalLayout_22.addWidget(Ui_MainWindow.tab3_page_listwidget)
        Ui_MainWindow.tab3_page_preview = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_8)
        Ui_MainWindow.tab3_page_preview.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab3_page_preview.setObjectName("tab3_page_preview")
        Ui_MainWindow.horizontalLayout_22.addWidget(Ui_MainWindow.tab3_page_preview)
        Ui_MainWindow.verticalLayout_12.addLayout(Ui_MainWindow.horizontalLayout_22)

        Ui_MainWindow.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_23.setObjectName("horizontalLayout_23")
        Ui_MainWindow.tab3_auto_play_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_auto_play_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_auto_play_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_auto_play_button.setObjectName("tab3_auto_play_button")
        Ui_MainWindow.horizontalLayout_23.addWidget(Ui_MainWindow.tab3_auto_play_button)

        Ui_MainWindow.tab3_play_page_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_play_page_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_play_page_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_play_page_button.setObjectName("tab3_play_page_button")
        Ui_MainWindow.horizontalLayout_23.addWidget(Ui_MainWindow.tab3_play_page_button)

        Ui_MainWindow.tab3_play_stop_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_play_stop_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_play_stop_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_play_stop_button.setObjectName("tab3_play_stop_button")
        Ui_MainWindow.horizontalLayout_23.addWidget(Ui_MainWindow.tab3_play_stop_button)

        Ui_MainWindow.verticalLayout_12.addLayout(Ui_MainWindow.horizontalLayout_23)

        Ui_MainWindow.horizontalLayout_20.addWidget(Ui_MainWindow.tab3_groupBox_8)
        Ui_MainWindow.verticalLayout_11 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_11.setObjectName("verticalLayout_11")
        Ui_MainWindow.tab3_groupBox_14 = QtWidgets.QGroupBox(Ui_MainWindow.tab3)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab3_groupBox_14.setFont(font)
        Ui_MainWindow.tab3_groupBox_14.setObjectName("tab3_groupBox_14")
        Ui_MainWindow.verticalLayout_14 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.verticalLayout_14.setObjectName("verticalLayout_14")
        Ui_MainWindow.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_24.setObjectName("horizontalLayout_24")
        Ui_MainWindow.tab3_test_color_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_test_color_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_test_color_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_test_color_button.setMinimumSize(QtCore.QSize(0, 40))
        Ui_MainWindow.tab3_test_color_button.setObjectName("tab3_test_color_button")
        Ui_MainWindow.horizontalLayout_24.addWidget(Ui_MainWindow.tab3_test_color_button)
        Ui_MainWindow.tab3_test_page_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_test_page_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_test_page_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_test_page_button.setMinimumSize(QtCore.QSize(0, 40))
        Ui_MainWindow.tab3_test_page_button.setObjectName("tab3_test_page_button")
        Ui_MainWindow.horizontalLayout_24.addWidget(Ui_MainWindow.tab3_test_page_button)
        Ui_MainWindow.tab3_view_finder_button = QtWidgets.QPushButton(Ui_MainWindow.tab3_groupBox_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_view_finder_button.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_view_finder_button.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_view_finder_button.setMinimumSize(QtCore.QSize(0, 40))
        Ui_MainWindow.tab3_view_finder_button.setObjectName("tab3_view_finder_button")
        Ui_MainWindow.horizontalLayout_24.addWidget(Ui_MainWindow.tab3_view_finder_button)
        Ui_MainWindow.verticalLayout_14.addLayout(Ui_MainWindow.horizontalLayout_24)
        Ui_MainWindow.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_25.setObjectName("horizontalLayout_25")
        Ui_MainWindow.tab3_voice_speed_display = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_voice_speed_display.setObjectName("tab3_voice_speed_display")
        Ui_MainWindow.horizontalLayout_25.addWidget(Ui_MainWindow.tab3_voice_speed_display)
        Ui_MainWindow.tab3_voice_speed_combobox = QtWidgets.QComboBox(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_voice_speed_combobox.setObjectName("tab3_voice_speed_combobox")
        Ui_MainWindow.horizontalLayout_25.addWidget(Ui_MainWindow.tab3_voice_speed_combobox)
        Ui_MainWindow.verticalLayout_14.addLayout(Ui_MainWindow.horizontalLayout_25)
        Ui_MainWindow.verticalLayout_13 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_13.setObjectName("verticalLayout_13")
        Ui_MainWindow.tab3_view_tracking_checkbox = QtWidgets.QCheckBox(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_view_tracking_checkbox.setObjectName("tab3_view_tracking_checkbox")
        Ui_MainWindow.verticalLayout_13.addWidget(Ui_MainWindow.tab3_view_tracking_checkbox)
        Ui_MainWindow.tab3_game_mode_checkbox = QtWidgets.QCheckBox(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_game_mode_checkbox.setObjectName("tab3_game_mode_checkbox")
        Ui_MainWindow.verticalLayout_13.addWidget(Ui_MainWindow.tab3_game_mode_checkbox)
        Ui_MainWindow.verticalLayout_14.addLayout(Ui_MainWindow.verticalLayout_13)
        Ui_MainWindow.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_26.setObjectName("horizontalLayout_26")
        Ui_MainWindow.tab3_male_voice_checkbox = QtWidgets.QRadioButton(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_male_voice_checkbox.setObjectName("tab3_male_voice_checkbox")
        Ui_MainWindow.horizontalLayout_26.addWidget(Ui_MainWindow.tab3_male_voice_checkbox)
        Ui_MainWindow.tab3_female_voice_checkbox = QtWidgets.QRadioButton(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_female_voice_checkbox.setObjectName("tab3_female_voice_checkbox")
        Ui_MainWindow.horizontalLayout_26.addWidget(Ui_MainWindow.tab3_female_voice_checkbox)
        Ui_MainWindow.verticalLayout_14.addLayout(Ui_MainWindow.horizontalLayout_26)
        Ui_MainWindow.verticalLayout_11.addWidget(Ui_MainWindow.tab3_groupBox_14)
        Ui_MainWindow.tab3_groupBox_15 = QtWidgets.QGroupBox(Ui_MainWindow.tab3)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab3_groupBox_15.setFont(font)
        Ui_MainWindow.tab3_groupBox_15.setObjectName("tab3_groupBox_15")
        Ui_MainWindow.verticalLayout_15 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab3_groupBox_15)
        Ui_MainWindow.verticalLayout_15.setObjectName("verticalLayout_15")
        Ui_MainWindow.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_27.setObjectName("horizontalLayout_27")
        Ui_MainWindow.tab3_page_display = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_page_display.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_page_display.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_page_display.setMinimumSize(QtCore.QSize(0, 30))
        Ui_MainWindow.tab3_page_display.setObjectName("tab3_page_display")
        Ui_MainWindow.horizontalLayout_27.addWidget(Ui_MainWindow.tab3_page_display)
        Ui_MainWindow.tab3_page_label = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_page_label.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_page_label.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_page_label.setMinimumSize(QtCore.QSize(0, 30))
        Ui_MainWindow.tab3_page_label.setObjectName("tab3_page_label")
        Ui_MainWindow.horizontalLayout_27.addWidget(Ui_MainWindow.tab3_page_label)
        Ui_MainWindow.verticalLayout_15.addLayout(Ui_MainWindow.horizontalLayout_27)
        Ui_MainWindow.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_28.setObjectName("horizontalLayout_28")
        Ui_MainWindow.tab3_label_display = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_label_display.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_label_display.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_label_display.setMinimumSize(QtCore.QSize(0, 30))
        Ui_MainWindow.tab3_label_display.setObjectName("tab3_label_display")
        Ui_MainWindow.horizontalLayout_28.addWidget(Ui_MainWindow.tab3_label_display)
        Ui_MainWindow.tab3_label_label = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        Ui_MainWindow.tab3_label_label.setMinimumSize(QtCore.QSize(0, 30))
        Ui_MainWindow.tab3_label_label.setObjectName("tab3_label_label")
        Ui_MainWindow.horizontalLayout_28.addWidget(Ui_MainWindow.tab3_label_label)
        Ui_MainWindow.verticalLayout_15.addLayout(Ui_MainWindow.horizontalLayout_28)
        Ui_MainWindow.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_29.setObjectName("horizontalLayout_29")
        Ui_MainWindow.tab3_textlabel_display = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab3_textlabel_display.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab3_textlabel_display.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab3_textlabel_display.setObjectName("tab3_textlabel_display")
        Ui_MainWindow.horizontalLayout_29.addWidget(Ui_MainWindow.tab3_textlabel_display)
        Ui_MainWindow.tab3_textlabel_label = QtWidgets.QLabel(Ui_MainWindow.tab3_groupBox_15)
        Ui_MainWindow.tab3_textlabel_label.setObjectName("tab3_textlabel_label")
        Ui_MainWindow.horizontalLayout_29.addWidget(Ui_MainWindow.tab3_textlabel_label)
        Ui_MainWindow.verticalLayout_15.addLayout(Ui_MainWindow.horizontalLayout_29)
        Ui_MainWindow.verticalLayout_11.addWidget(Ui_MainWindow.tab3_groupBox_15)
        Ui_MainWindow.horizontalLayout_20.addLayout(Ui_MainWindow.verticalLayout_11)
        Ui_MainWindow.verticalLayout_16.addLayout(Ui_MainWindow.horizontalLayout_20)

        # comment below if you want those tabs.
        Ui_MainWindow.tab3_groupBox_15.setVisible(False)
        Ui_MainWindow.tab3_groupBox_14.setVisible(False)
        Ui_MainWindow.tab3_auto_play_button.setVisible(False)

        Tab3Create.__retranslate_ui(Ui_MainWindow)
        Tab3Create.__set_tool_tips(Ui_MainWindow)
        Tab3Create.__set_up_click_events(Ui_MainWindow)
    
    
    def __retranslate_ui(Ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow.tab3_groupBox_6.setTitle(_translate("MainWindow", "Book"))
        Ui_MainWindow.tab3_book_display.setText(_translate("MainWindow", "Book1"))
        Ui_MainWindow.tab3_select_book.setText(_translate("MainWindow", "Select"))
        Ui_MainWindow.tab3_groupBox_7.setTitle(_translate("MainWindow", "Chapter"))
        Ui_MainWindow.tab3_chapter_label.setText(_translate("MainWindow", "Select Chapter"))
        Ui_MainWindow.tab3_groupBox_8.setTitle(_translate("MainWindow", "Pages"))
        Ui_MainWindow.tab3_page_preview.setText(_translate("MainWindow", "Page Preview"))
        Ui_MainWindow.tab3_auto_play_button.setText(_translate("MainWindow", "Auto Play"))
        Ui_MainWindow.tab3_play_page_button.setText(_translate("MainWindow", "Play Page"))
        Ui_MainWindow.tab3_play_stop_button.setText(_translate("MainWindow", "Stop Play"))
        Ui_MainWindow.tab3_groupBox_14.setTitle(_translate("MainWindow", "Tracking Option"))
        Ui_MainWindow.tab3_test_color_button.setText(_translate("MainWindow", "Test Color Detection"))
        Ui_MainWindow.tab3_test_page_button.setText(_translate("MainWindow", "Test Page Detection"))
        Ui_MainWindow.tab3_view_finder_button.setText(_translate("MainWindow", "View Finder"))
        Ui_MainWindow.tab3_voice_speed_display.setText(_translate("MainWindow", "Voice Speed"))
        Ui_MainWindow.tab3_view_tracking_checkbox.setText(_translate("MainWindow", "View Tracking"))
        Ui_MainWindow.tab3_game_mode_checkbox.setText(_translate("MainWindow", "GAME MODE"))
        Ui_MainWindow.tab3_male_voice_checkbox.setText(_translate("MainWindow", "MALE Voice"))
        Ui_MainWindow.tab3_female_voice_checkbox.setText(_translate("MainWindow", "FEMALE Voice"))

        Ui_MainWindow.tab3_groupBox_15.setTitle(_translate("MainWindow", "Now Playing"))
        Ui_MainWindow.tab3_page_display.setText(_translate("MainWindow", "PAGE : "))
        Ui_MainWindow.tab3_page_label.setText(_translate("MainWindow", "Yolo"))
        Ui_MainWindow.tab3_label_display.setText(_translate("MainWindow", "LABEL : "))
        Ui_MainWindow.tab3_label_label.setText(_translate("MainWindow", "Lol"))
        Ui_MainWindow.tab3_textlabel_display.setText(_translate("MainWindow", "TextLabel"))
        Ui_MainWindow.tab3_textlabel_label.setText(_translate("MainWindow", "TextLabel"))


    def __set_tool_tips(Ui_MainWindow):
        pass


    def __set_up_click_events(Ui_MainWindow):
        Ui_MainWindow.invoker_tab3=invoker.Invoker(Ui_MainWindow)

        Ui_MainWindow.tab3_select_book.clicked.connect(Ui_MainWindow.invoker_tab3.select_book)

        #Ui_MainWindow.tab3_page_listwidget.itemClicked.connect(Ui_MainWindow.invoker_tab3.select_page)

        Ui_MainWindow.tab3_select_chapter_combobox.activated.connect(Ui_MainWindow.invoker_tab3.select_chapter)

        Ui_MainWindow.tab3_play_page_button.clicked.connect(Ui_MainWindow.invoker_tab3.play_page)

        Ui_MainWindow.tab3_play_stop_button.clicked.connect(Ui_MainWindow.invoker_tab3.stop_page)





