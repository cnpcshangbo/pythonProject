#!/usr/bin/env python3
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from drillingui import Ui_Form
from mySubprocessui import Ui_Form_subprocess


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_subprocess()
        self.ui.setupUi(self)
        #print(self.ui)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.say_hello)
        self.ui.pushButton_2.clicked.connect(self.toggle_window1)
        self.ui.pushButton_3.clicked.connect(self.toggle_window2)
        # self.ui.pushButton.setStyleSheet("color: blue;"
        #                "background-color: yellow;"
        #                "selection-color: yellow;"
        #                "selection-background-color: blue;")
        # print(self.ui.pushButton)
        # self.ui.label_3.setText("test")

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()


    @staticmethod
    def say_hello():
        """

        """
        print("button clicked")
        # subprocess.call("python mySubprocess.py", shell=True)
        # exec(open("mySubprocess.py").read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()

    window.show()


    sys.exit(app.exec())
