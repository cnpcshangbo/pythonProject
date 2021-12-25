#!/usr/bin/env python3
import logging
import subprocess
import sys
import threading
import time
import signal

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

        # stdout = subprocess.check_output(' '.join(['sh -c', '\"source ~/ros_noetic_bare_bone_catkin_ws/install_isolated/setup.sh &&', self.ui.lineEdit.text(), "\""]), shell=True)

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        # if self.p is None:
        # try:
        #     self.p
        # except NameError:
        if not hasattr(self, 'p'):
            logging.info("Creating Pipe.")
            self.p = subprocess.Popen(["python", "1st.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            x = threading.Thread(target=self.thread_function, args=(1,))
            x.start()

        # self.p.stdin.write(self.ui.lineEdit.text().encode())
        self.p.stdin.write(''.join([self.ui.lineEdit.text(), '\n']).encode())
        self.p.stdin.flush()  # not necessary in this case
        # get output from process "not time to break"
        # one_line_output = p.stdout.readline()
        print("sent" + self.ui.lineEdit.text())

        # time.sleep(2)
        # # write "n\n" to that process for if r=='n':
        # self.p.stdin.write(self.ui.lineEdit.text().encode())
        # self.p.stdin.flush()  # not necessary in this case

        # self.ui.textEdit.setText(stdout.decode("utf-8"))
        # self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())

    # self.ui.label_3.setText("test")

    def thread_function(self, name):
        logging.info("Thread %s: starting", name)
        # get output from process "Something to print"
        while True:
            time.sleep(0.1)
            one_line_output = self.p.stdout.readline()
            logging.info("Thread %s: running", name)
            logging.info(one_line_output)

            if one_line_output == b"":
                logging.info("Thread %s: finishing", name)
                break


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)


signal.signal(signal.SIGINT, handler)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
