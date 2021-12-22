import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from mySubprocessui import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        print(self.ui)
        #self.ui.label_3.setText("test")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
