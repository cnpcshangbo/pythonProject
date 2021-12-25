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
        print("AnotherWindow init.")
        self.setWindowTitle(type(self).__name__)
        self.ui.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        """

        """
        print("button clicked")
        # self.ui.textEdit.setText(str(subprocess.call("ls", shell=True)))
        # exec(open("mySubprocess.py").read())
        MyOut = subprocess.Popen(self.ui.lineEdit.text(), shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, stderr = MyOut.communicate()
        print(stdout)
        print(stderr)
        self.ui.textEdit.setText(stdout.decode("utf-8"))
        self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())


class RunMavros(AnotherWindow):
    def __init__(self):
        super().__init__()
        # self.ui.move(0, 0)
        print("RunMavros init.")
        self.setGeometry(400, 00, 300, 300)
        self.setWindowTitle("(1)" + self.windowTitle())
        self.ui.lineEdit.setText("roslaunch mavros px4mst.launch")


class RunVicon(AnotherWindow):
    def __init__(self):
        super().__init__()
        print("Vicon init.")
        self.setGeometry(700, 00, 300, 300)
        self.setWindowTitle("(2)" + self.windowTitle())
        self.ui.lineEdit.setText("roslaunch vicon_bridge vicon.launch")


class RunTalker(AnotherWindow):
    def __init__(self):
        super().__init__()
        print("Vicon init.")
        self.setGeometry(1000, 00, 300, 300)
        self.setWindowTitle("(3)" + self.windowTitle())
        self.ui.lineEdit.setText("rosrun vicon_to_mavros talker")


class RunSetPoint(AnotherWindow):
    def __init__(self):
        super().__init__()
        # print("Vicon init.")
        self.setGeometry(1400, 00, 300, 300)
        self.setWindowTitle("(4)" + self.windowTitle())
        self.ui.lineEdit.setText("rosrun flight_test flight_test_setpoint_drill")


class RunPID(AnotherWindow):
    def __init__(self):
        super().__init__()
        # print("Vicon init.")
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle("(5)" + self.windowTitle())
        self.ui.lineEdit.setText("rosrun flight_test flight_test_pid_drill")


class RunDrillSense(AnotherWindow):
    def __init__(self):
        super().__init__()
        # print("Vicon init.")
        self.setGeometry(1100, 400, 300, 300)
        self.setWindowTitle("(6)T=1,S=1. " + self.windowTitle())
        self.ui.lineEdit.setText('rosrun drillpress_pack Drillpress_node')


class RunLockRelease(AnotherWindow):
    def __init__(self):
        super().__init__()
        # print("Vicon init.")
        self.setGeometry(1100, 700, 300, 300)
        self.setWindowTitle("(7)1,0,2,type Raw in (6)" + self.windowTitle())
        self.ui.lineEdit.setText('rosrun drillpress_pack UAV_drillsensor')


class RunRosBag(AnotherWindow):
    def __init__(self):
        super().__init__()
        # print("Vicon init.")
        self.setGeometry(1400, 700, 300, 300)
        self.setWindowTitle("(8)" + self.windowTitle())
        self.ui.lineEdit.setText('rosbag record -a')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window0 = RunMavros()
        self.window1 = RunVicon()
        self.window2 = RunTalker()
        self.window3 = RunSetPoint()
        self.window4 = RunPID()
        self.window5 = RunDrillSense()
        self.window6 = RunLockRelease()
        self.window7 = RunRosBag()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.toggle_window0)
        self.ui.pushButton_2.clicked.connect(self.toggle_window1)
        self.ui.pushButton_3.clicked.connect(self.toggle_window2)
        self.ui.pushButton_4.clicked.connect(self.toggle_window3)
        self.ui.pushButton_5.clicked.connect(self.toggle_window4)
        self.ui.pushButton_6.clicked.connect(self.toggle_window5)
        self.ui.pushButton_7.clicked.connect(self.toggle_window6)
        self.ui.pushButton_8.clicked.connect(self.toggle_window7)
        # self.ui.pushButton.setStyleSheet("color: blue;"
        #                "background-color: yellow;"
        #                "selection-color: yellow;"
        #                "selection-background-color: blue;")
        # print(self.ui.pushButton)
        # self.ui.label_3.setText("test")
        self.setGeometry(0, 0, 400, 700)
        # print(self.geometry())

    def toggle_window0(self, checked):
        if self.window0.isVisible():
            self.window0.hide()

        else:
            self.window0.show()

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

    def toggle_window3(self, checked):
        if self.window3.isVisible():
            self.window3.hide()

        else:
            self.window3.show()

    def toggle_window4(self, checked):
        if self.window4.isVisible():
            self.window4.hide()

        else:
            self.window4.show()

    def toggle_window5(self, checked):
        if self.window5.isVisible():
            self.window5.hide()

        else:
            self.window5.show()

    def toggle_window6(self, checked):
        if self.window6.isVisible():
            self.window6.hide()

        else:
            self.window6.show()

    def toggle_window7(self, checked):
        if self.window7.isVisible():
            self.window7.hide()

        else:
            self.window7.show()

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
