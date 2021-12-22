# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from PyQt6 import QtGui
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import subprocess
from ui import Ui_Form


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


class Window(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.handlebutton)

    @staticmethod
    def handlebutton():
        print('Hello World!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
