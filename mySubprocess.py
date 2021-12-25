#!/usr/bin/env python3
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QWidget

from mySubprocessui import Ui_Form_subprocess


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form_subprocess()
        self.ui.setupUi(self)
        # self.move(0, 0)
        self.setGeometry(0, 0, 300, 300)
        print(self.geometry())
        print(self.ui)
        self.ui.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        """

        """
        print("button clicked")
        # self.ui.textEdit.setText(str(subprocess.call("ls", shell=True)))
        # exec(open("mySubprocess.py").read())
        # MyOut = subprocess.Popen(self.ui.lineEdit.text(), shell=True,
        #                          stdout=subprocess.PIPE,
        #                          stderr=subprocess.STDOUT)
        # stdout, stderr = MyOut.communicate()
        # print(stdout)
        # print(stderr)

        stdout = subprocess.check_output(' '.join(['sh -c', '\"source ~/ros_noetic_bare_bone_catkin_ws/install_isolated/setup.sh &&', self.ui.lineEdit.text(), "\""]), shell=True)
        self.ui.textEdit.setText(stdout.decode("utf-8"))
        self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())

# self.ui.label_3.setText("test")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
