#!/usr/bin/env python3
import logging
import subprocess
import sys
import threading
import time

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
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        print("button clicked")
        # self.ui.textEdit.setText(str(subprocess.call("ls", shell=True)))
        # exec(open("mySubprocess.py").read())
        if not hasattr(self, 'p'):
            logging.info("Creating Pipe.")
            self.p = subprocess.Popen(self.ui.lineEdit.text(), shell=True, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/zsh')
            # self.p = subprocess.Popen(["python", "1st.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            x = threading.Thread(target=self.thread_function, args=(1,))
            x.start()
        else:
            # self.p.stdin.write(self.ui.lineEdit.text().encode())
            self.p.stdin.write(''.join([self.ui.lineEdit.text(), '\n']).encode())
            try:
                self.p.stdin.flush()  # not necessary in this case
            # except NameError:
            #     self.p = subprocess.Popen(self.ui.lineEdit.text(), shell=True, stdin=subprocess.PIPE,
            #                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, checked = True)
            except:
                self.p = subprocess.Popen(self.ui.lineEdit.text(), shell=True, stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable='/bin/zsh')
                x = threading.Thread(target=self.thread_function, args=(1,))
                x.start()


            # get output from process "not time to break"
            # one_line_output = p.stdout.readline()
            print("sent" + self.ui.lineEdit.text())

            # MyOut = subprocess.Popen(self.ui.lineEdit.text(), shell=True,
            #                          stdout=subprocess.PIPE,
            #                          stderr=subprocess.STDOUT)
            # stdout, stderr = MyOut.communicate()
            # print(stdout)
            # print(stderr)
            # self.ui.textEdit.setText(stdout.decode("utf-8"))
            # self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())

    def thread_function(self, name):
        logging.info("Thread %s: starting", name)
        # get output from process "Something to print"
        while True:
            time.sleep(0.1)
            one_line_output = self.p.stdout.readline()
            logging.info("Thread %s: running", name)
            logging.info(one_line_output)
            self.ui.textEdit.append(one_line_output.decode("utf-8"))
            self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())


            if one_line_output == b"":
                logging.info("Thread %s: finishing", name)
                break


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
