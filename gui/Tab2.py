

from PyQt5 import QtCore, QtGui, QtWidgets

import controller.tab2_controller.Invoker as invoker
class Tab2Create:

    def intiate(self,Ui_MainWindow):

        Ui_MainWindow.tab2 = QtWidgets.QWidget()
        Ui_MainWindow.tab2.setObjectName("tab2")
        Ui_MainWindow.verticalLayout_6 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab2)
        Ui_MainWindow.verticalLayout_6.setObjectName("verticalLayout_6")
        Ui_MainWindow.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_9.setObjectName("horizontalLayout_9")
        Ui_MainWindow.tab2_groupBox_9 = QtWidgets.QGroupBox(Ui_MainWindow.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_groupBox_9.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_groupBox_9.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_groupBox_9.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainWindow.tab2_groupBox_9.setFont(font)
        Ui_MainWindow.tab2_groupBox_9.setObjectName("tab2_groupBox_9")
        Ui_MainWindow.horizontalLayout_11 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab2_groupBox_9)
        Ui_MainWindow.horizontalLayout_11.setObjectName("horizontalLayout_11")
        Ui_MainWindow.tab2_book_name_2 = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_9)
        Ui_MainWindow.tab2_book_name_2.setObjectName("tab2_book_name_2")
        Ui_MainWindow.horizontalLayout_11.addWidget(Ui_MainWindow.tab2_book_name_2)

        ##Select book group box
        Ui_MainWindow.tab2_select_book_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_9)

        Ui_MainWindow.tab2_select_book_button.setObjectName("tab2_select_book_button")
        Ui_MainWindow.horizontalLayout_11.addWidget(Ui_MainWindow.tab2_select_book_button)
        Ui_MainWindow.horizontalLayout_9.addWidget(Ui_MainWindow.tab2_groupBox_9)

        Ui_MainWindow.tab2_new_book = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_9)
        Ui_MainWindow.tab2_new_book.setObjectName("tab2_new_book")
        Ui_MainWindow.horizontalLayout_11.addWidget(Ui_MainWindow.tab2_new_book)

        Ui_MainWindow.tab2_delete_book = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_9)
        Ui_MainWindow.tab2_delete_book.setObjectName("tab2_delete_book")
        Ui_MainWindow.horizontalLayout_11.addWidget(Ui_MainWindow.tab2_delete_book)
        ##


        Ui_MainWindow.tab2_groupBox_10 = QtWidgets.QGroupBox(Ui_MainWindow.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_groupBox_10.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_groupBox_10.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_groupBox_10.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ui_MainWindow.tab2_groupBox_10.setFont(font)

        ##Select chapter group Box
        Ui_MainWindow.tab2_groupBox_10.setObjectName("tab2_groupBox_10")
        Ui_MainWindow.horizontalLayout_12 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.horizontalLayout_12.setObjectName("horizontalLayout_12")
        Ui_MainWindow.tab2_chapter_name = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.tab2_chapter_name.setObjectName("tab2_chapter_name")
        Ui_MainWindow.horizontalLayout_12.addWidget(Ui_MainWindow.tab2_chapter_name)

        Ui_MainWindow.tab2_chapter_select_combobox = QtWidgets.QComboBox(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.tab2_chapter_select_combobox.setObjectName("tab2_chapter_select_combobox")
        Ui_MainWindow.horizontalLayout_12.addWidget(Ui_MainWindow.tab2_chapter_select_combobox)

        Ui_MainWindow.tab2_new_chapter = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.tab2_new_chapter.setObjectName("tab2_new_chapter")
        Ui_MainWindow.horizontalLayout_12.addWidget(Ui_MainWindow.tab2_new_chapter)

        Ui_MainWindow.tab2_delete_chapter = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.tab2_delete_chapter.setObjectName("tab2_delete_chapter")
        Ui_MainWindow.horizontalLayout_12.addWidget(Ui_MainWindow.tab2_delete_chapter)
        ##

        Ui_MainWindow.horizontalLayout_9.addWidget(Ui_MainWindow.tab2_groupBox_10)
        Ui_MainWindow.verticalLayout_6.addLayout(Ui_MainWindow.horizontalLayout_9)
        Ui_MainWindow.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_10.setObjectName("horizontalLayout_10")
        Ui_MainWindow.verticalLayout_7 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_7.setObjectName("verticalLayout_7")

        ##Group Box Page
        Ui_MainWindow.tab2_groupBox_12 = QtWidgets.QGroupBox(Ui_MainWindow.tab2)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab2_groupBox_12.setFont(font)
        Ui_MainWindow.tab2_groupBox_12.setObjectName("tab2_groupBox_12")
        Ui_MainWindow.horizontalLayout_7 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab2_groupBox_12)
        Ui_MainWindow.horizontalLayout_7.setObjectName("horizontalLayout_7")
        Ui_MainWindow.verticalLayout_8 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_8.setObjectName("verticalLayout_8")
        Ui_MainWindow.tab2_page_listwidget = QtWidgets.QListWidget(Ui_MainWindow.tab2_groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_page_listwidget.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_page_listwidget.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_page_listwidget.setObjectName("tab2_page_listwidget")
        Ui_MainWindow.verticalLayout_8.addWidget(Ui_MainWindow.tab2_page_listwidget)

        Ui_MainWindow.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_30.setObjectName("horizontalLayout_30")


        Ui_MainWindow.tab2_new_page = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_12)
        Ui_MainWindow.tab2_new_page.setObjectName("tab2_new_page")
        Ui_MainWindow.horizontalLayout_30.addWidget(Ui_MainWindow.tab2_new_page)

        Ui_MainWindow.tab2_delete_page = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_12)
        Ui_MainWindow.tab2_delete_page.setObjectName("tab2_delete_page")
        Ui_MainWindow.horizontalLayout_30.addWidget(Ui_MainWindow.tab2_delete_page)

        Ui_MainWindow.verticalLayout_8.addLayout(Ui_MainWindow.horizontalLayout_30)


        Ui_MainWindow.horizontalLayout_7.addLayout(Ui_MainWindow.verticalLayout_8)
        Ui_MainWindow.tab2_page_preview = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_page_preview.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_page_preview.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_page_preview.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab2_page_preview.setObjectName("tab2_page_preview")


        Ui_MainWindow.horizontalLayout_7.addWidget(Ui_MainWindow.tab2_page_preview)
        Ui_MainWindow.verticalLayout_7.addWidget(Ui_MainWindow.tab2_groupBox_12)
        Ui_MainWindow.tab2_groupBox_13 = QtWidgets.QGroupBox(Ui_MainWindow.tab2)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab2_groupBox_13.setFont(font)
        Ui_MainWindow.tab2_groupBox_13.setObjectName("tab2_groupBox_13")
        Ui_MainWindow.horizontalLayout_8 = QtWidgets.QHBoxLayout(Ui_MainWindow.tab2_groupBox_13)
        Ui_MainWindow.horizontalLayout_8.setObjectName("horizontalLayout_8")
        Ui_MainWindow.verticalLayout_9 = QtWidgets.QVBoxLayout()
        Ui_MainWindow.verticalLayout_9.setObjectName("verticalLayout_9")
        Ui_MainWindow.tab2_label_listwidget = QtWidgets.QListWidget(Ui_MainWindow.tab2_groupBox_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_label_listwidget.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_label_listwidget.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_label_listwidget.setObjectName("tab2_label_listwidget")
        Ui_MainWindow.verticalLayout_9.addWidget(Ui_MainWindow.tab2_label_listwidget)
        Ui_MainWindow.tab2_delete_label_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_13)
        Ui_MainWindow.tab2_delete_label_button.setObjectName("tab2_delete_label_button")
        Ui_MainWindow.verticalLayout_9.addWidget(Ui_MainWindow.tab2_delete_label_button)
        Ui_MainWindow.horizontalLayout_8.addLayout(Ui_MainWindow.verticalLayout_9)
        Ui_MainWindow.tab2_label_preview = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_13)
        Ui_MainWindow.tab2_label_preview.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab2_label_preview.setObjectName("tab2_label_preview")
        Ui_MainWindow.horizontalLayout_8.addWidget(Ui_MainWindow.tab2_label_preview)
        Ui_MainWindow.verticalLayout_7.addWidget(Ui_MainWindow.tab2_groupBox_13)
        Ui_MainWindow.horizontalLayout_10.addLayout(Ui_MainWindow.verticalLayout_7)
        Ui_MainWindow.tab2_groupBox_11 = QtWidgets.QGroupBox(Ui_MainWindow.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_groupBox_11.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_groupBox_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        Ui_MainWindow.tab2_groupBox_11.setFont(font)
        Ui_MainWindow.tab2_groupBox_11.setObjectName("tab2_groupBox_11")
        Ui_MainWindow.verticalLayout_10 = QtWidgets.QVBoxLayout(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.verticalLayout_10.setObjectName("verticalLayout_10")
        Ui_MainWindow.tab2_add_label_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_add_label_button.setObjectName("tab2_add_label_button")
        Ui_MainWindow.verticalLayout_10.addWidget(Ui_MainWindow.tab2_add_label_button)
        Ui_MainWindow.tab2_spacer1_2 = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_spacer1_2.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_spacer1_2.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_spacer1_2.setText("")
        Ui_MainWindow.tab2_spacer1_2.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab2_spacer1_2.setObjectName("tab2_spacer1_2")
        Ui_MainWindow.verticalLayout_10.addWidget(Ui_MainWindow.tab2_spacer1_2)
        Ui_MainWindow.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_13.setObjectName("horizontalLayout_13")
        Ui_MainWindow.tab2_label_display = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_label_display.setObjectName("tab2_label_display")
        Ui_MainWindow.horizontalLayout_13.addWidget(Ui_MainWindow.tab2_label_display)
        Ui_MainWindow.tab2_label_input = QtWidgets.QLineEdit(Ui_MainWindow.tab2_groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_label_input.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_label_input.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_label_input.setObjectName("tab2_label_input")
        Ui_MainWindow.horizontalLayout_13.addWidget(Ui_MainWindow.tab2_label_input)
        Ui_MainWindow.verticalLayout_10.addLayout(Ui_MainWindow.horizontalLayout_13)
        Ui_MainWindow.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_14.setObjectName("horizontalLayout_14")
        Ui_MainWindow.tab2_label_select_audio_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_label_select_audio_button.setObjectName("tab2_label_select_audio_button")
        Ui_MainWindow.horizontalLayout_14.addWidget(Ui_MainWindow.tab2_label_select_audio_button)
        Ui_MainWindow.tab2_label_audio_file = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_label_audio_file.setObjectName("tab2_label_audio_file")
        Ui_MainWindow.horizontalLayout_14.addWidget(Ui_MainWindow.tab2_label_audio_file)
        Ui_MainWindow.verticalLayout_10.addLayout(Ui_MainWindow.horizontalLayout_14)
        Ui_MainWindow.tab2_spacer2_2 = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_spacer2_2.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_spacer2_2.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_spacer2_2.setText("")
        Ui_MainWindow.tab2_spacer2_2.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab2_spacer2_2.setObjectName("tab2_spacer2_2")
        Ui_MainWindow.verticalLayout_10.addWidget(Ui_MainWindow.tab2_spacer2_2)
        Ui_MainWindow.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_15.setObjectName("horizontalLayout_15")
        Ui_MainWindow.tab2_description_display = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_description_display.setObjectName("tab2_description_display")
        Ui_MainWindow.horizontalLayout_15.addWidget(Ui_MainWindow.tab2_description_display)
        Ui_MainWindow.tab2_description_input = QtWidgets.QTextEdit(Ui_MainWindow.tab2_groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_description_input.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_description_input.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_description_input.setObjectName("tab2_description_input")
        Ui_MainWindow.horizontalLayout_15.addWidget(Ui_MainWindow.tab2_description_input)
        Ui_MainWindow.verticalLayout_10.addLayout(Ui_MainWindow.horizontalLayout_15)
        Ui_MainWindow.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        Ui_MainWindow.horizontalLayout_16.setObjectName("horizontalLayout_16")
        Ui_MainWindow.tab2_description_select_audio_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_description_select_audio_button.setObjectName("tab2_description_select_audio_button")
        Ui_MainWindow.horizontalLayout_16.addWidget(Ui_MainWindow.tab2_description_select_audio_button)
        Ui_MainWindow.tab2_description_audio_file = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_description_audio_file.setObjectName("tab2_description_audio_file")
        Ui_MainWindow.horizontalLayout_16.addWidget(Ui_MainWindow.tab2_description_audio_file)
        Ui_MainWindow.verticalLayout_10.addLayout(Ui_MainWindow.horizontalLayout_16)
        Ui_MainWindow.tab2_spacer3_2 = QtWidgets.QLabel(Ui_MainWindow.tab2_groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_MainWindow.tab2_spacer3_2.sizePolicy().hasHeightForWidth())
        Ui_MainWindow.tab2_spacer3_2.setSizePolicy(sizePolicy)
        Ui_MainWindow.tab2_spacer3_2.setText("")
        Ui_MainWindow.tab2_spacer3_2.setAlignment(QtCore.Qt.AlignCenter)
        Ui_MainWindow.tab2_spacer3_2.setObjectName("tab2_spacer3_2")
        Ui_MainWindow.verticalLayout_10.addWidget(Ui_MainWindow.tab2_spacer3_2)
        Ui_MainWindow.tab2_save_label_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_save_label_button.setObjectName("tab2_save_label_button")
        Ui_MainWindow.verticalLayout_10.addWidget(Ui_MainWindow.tab2_save_label_button)
        Ui_MainWindow.horizontalLayout_10.addWidget(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.verticalLayout_6.addLayout(Ui_MainWindow.horizontalLayout_10)

        # Changing requirements damn
        Ui_MainWindow.tab2_start_recording_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_start_recording_button.setObjectName("tab2_start_recording_button")
        Ui_MainWindow.horizontalLayout_15.addWidget(Ui_MainWindow.tab2_start_recording_button)

        Ui_MainWindow.tab2_stop_recording_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_stop_recording_button.setObjectName("tab2_stop_recording_button")
        Ui_MainWindow.horizontalLayout_15.addWidget(Ui_MainWindow.tab2_stop_recording_button)

        Ui_MainWindow.tab2_play_recording_button = QtWidgets.QPushButton(Ui_MainWindow.tab2_groupBox_11)
        Ui_MainWindow.tab2_play_recording_button.setObjectName("tab2_play_recording_button")
        Ui_MainWindow.horizontalLayout_15.addWidget(Ui_MainWindow.tab2_play_recording_button)


        Ui_MainWindow.tab2_description_display.setVisible(False)
        Ui_MainWindow.tab2_description_input.setVisible(False)
        Ui_MainWindow.tab2_label_select_audio_button.setVisible(False)
        Ui_MainWindow.tab2_description_audio_file.setVisible(False)

        Tab2Create.__retranslate_ui(Ui_MainWindow)
        Tab2Create.__set_up_click_events(Ui_MainWindow)












    def __retranslate_ui(Ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate

        Ui_MainWindow.tab2_groupBox_9.setTitle(_translate("MainWindow", "Book"))
        Ui_MainWindow.tab2_book_name_2.setText(_translate("MainWindow", "Book1"))
        Ui_MainWindow.tab2_select_book_button.setText(_translate("MainWindow", "Select"))
        Ui_MainWindow.tab2_new_book.setText(_translate("MainWindow","New"))
        Ui_MainWindow.tab2_delete_book.setText(_translate("MainWindow", "Delete"))

        Ui_MainWindow.tab2_groupBox_10.setTitle(_translate("MainWindow", "Chapter"))
        Ui_MainWindow.tab2_chapter_name.setText(_translate("MainWindow", "Select Chapter"))
        Ui_MainWindow.tab2_new_chapter.setText(_translate("MainWindow", "New"))
        Ui_MainWindow.tab2_delete_chapter.setText(_translate("MainWindow", "Delete"))

        Ui_MainWindow.tab2_groupBox_12.setTitle(_translate("MainWindow", "Pages"))
        Ui_MainWindow.tab2_delete_page.setText(_translate("MainWindow", "Delete Page"))
        Ui_MainWindow.tab2_new_page.setText(_translate("MainWindow","Add Page"))
        Ui_MainWindow.tab2_page_preview.setText(_translate("MainWindow", "Page Preview"))

        Ui_MainWindow.tab2_groupBox_13.setTitle(_translate("MainWindow", "Labels"))
        Ui_MainWindow.tab2_delete_label_button.setText(_translate("MainWindow", "Delete Label"))
        Ui_MainWindow.tab2_label_preview.setText(_translate("MainWindow", "Label Preview"))

        Ui_MainWindow.tab2_groupBox_11.setTitle(_translate("MainWindow", "Label Creation"))
        Ui_MainWindow.tab2_add_label_button.setText(_translate("MainWindow", "Add New Label"))
        Ui_MainWindow.tab2_label_display.setText(_translate("MainWindow", "Label : "))
        Ui_MainWindow.tab2_label_select_audio_button.setText(_translate("MainWindow", "Select Audio File"))
        Ui_MainWindow.tab2_label_audio_file.setText(_translate("MainWindow", "No File Selected"))
        Ui_MainWindow.tab2_description_display.setText(_translate("MainWindow", "Description"))
        Ui_MainWindow.tab2_description_select_audio_button.setText(_translate("MainWindow", "Select Audio File"))
        Ui_MainWindow.tab2_description_audio_file.setText(_translate("MainWindow", "No File Selected"))
        Ui_MainWindow.tab2_save_label_button.setText(_translate("MainWindow", "Save Label"))

        Ui_MainWindow.tab2_start_recording_button.setText(_translate("MainWindow", "Start Recording"))
        Ui_MainWindow.tab2_stop_recording_button.setText(_translate("MainWindow", "Stop Recording"))
        Ui_MainWindow.tab2_play_recording_button.setText(_translate("MainWindow", "Play Recorded"))




    def __set_tool_tips(Ui_MainWindow):
        pass

    def __set_up_click_events(Ui_MainWindow):
        Ui_MainWindow.invoker_tab2=invoker.Invoker(Ui_MainWindow)

        ##tab1 imports
        Ui_MainWindow.tab2_new_book.clicked.connect(Ui_MainWindow.invoker_tab2.new_book)
        Ui_MainWindow.tab2_delete_book.clicked.connect(Ui_MainWindow.invoker_tab2.delete_book)
        Ui_MainWindow.tab2_new_chapter.clicked.connect(Ui_MainWindow.invoker_tab2.new_chapter)
        Ui_MainWindow.tab2_delete_chapter.clicked.connect(Ui_MainWindow.invoker_tab2.delete_chapter)
        Ui_MainWindow.tab2_new_page.clicked.connect(Ui_MainWindow.invoker_tab2.new_page)

        Ui_MainWindow.tab2_select_book_button.clicked.connect(Ui_MainWindow.invoker_tab2.select_book)
        Ui_MainWindow.tab2_save_label_button.clicked.connect(Ui_MainWindow.invoker_tab2.save_label)
        Ui_MainWindow.tab2_label_select_audio_button.clicked.connect(Ui_MainWindow.invoker_tab2.select_audio_label)
        Ui_MainWindow.tab2_description_select_audio_button.clicked.connect(Ui_MainWindow.invoker_tab2.select_audio_description)
        Ui_MainWindow.tab2_delete_label_button.clicked.connect(Ui_MainWindow.invoker_tab2.delete_label)
        Ui_MainWindow.tab2_delete_page.clicked.connect(Ui_MainWindow.invoker_tab2.delete_page)
        Ui_MainWindow.tab2_add_label_button.clicked.connect(Ui_MainWindow.invoker_tab2.add_new_label)

        Ui_MainWindow.tab2_label_listwidget.itemClicked.connect(Ui_MainWindow.invoker_tab2.select_label)
        Ui_MainWindow.tab2_page_listwidget.itemClicked.connect(Ui_MainWindow.invoker_tab2.select_page)


        Ui_MainWindow.tab2_chapter_select_combobox.activated.connect(Ui_MainWindow.invoker_tab2.select_chapter)

        Ui_MainWindow.tab2_start_recording_button.clicked.connect(Ui_MainWindow.invoker_tab2.start_recording)
        Ui_MainWindow.tab2_stop_recording_button.clicked.connect(Ui_MainWindow.invoker_tab2.stop_recording)
        Ui_MainWindow.tab2_play_recording_button.clicked.connect(Ui_MainWindow.invoker_tab2.play_recording)










