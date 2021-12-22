# File: main.py
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "ui.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    print(window)
    window.setWindowTitle("Serial demo 2")
    button = QPushButton("Press Me!")

    # Set the central widget of the Window.
    #window.Width = 1000
    #print(window.geometry)
    window.label_2.setText("Messages.-----")
    window.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 0, 0)\n"
"}")
    window.show()

    sys.exit(app.exec())
