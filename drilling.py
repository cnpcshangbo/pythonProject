#!/usr/bin/env python3
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from drillingui import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.say_hello)
        # self.ui.pushButton.setStyleSheet("color: blue;"
        #                "background-color: yellow;"
        #                "selection-color: yellow;"
        #                "selection-background-color: blue;")
        print(self.ui.pushButton)
        # self.ui.label_3.setText("test")

    @staticmethod
    def say_hello():
        """

        """
        print("button clicked")
        subprocess.call("python mySubprocess.py", shell=True)
        # exec(open("mySubprocess.py").read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
