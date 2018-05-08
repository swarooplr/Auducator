import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import gui.MainWindowGUI
import gui.Tab1 as tab1
class MainWindow(QMainWindow,gui.MainWindowGUI.Ui_MainWindow):
        def __init__(self):
            super(MainWindow,self).__init__()
            self.setupUi(self)


def main():
    app=QApplication(sys.argv)
    main_window=MainWindow()
    main_window.show()
    sys.exit(app.exec())


main()
