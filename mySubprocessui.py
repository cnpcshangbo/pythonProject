# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mySubprocess.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form_subprocess(object):
    def setupUi(self, Form_subprocess):
        if not Form_subprocess.objectName():
            Form_subprocess.setObjectName(u"Form_subprocess")
        Form_subprocess.resize(297, 325)
        Form_subprocess.setStyleSheet(u"QLabel{\n"
"	font: 18pt \".AppleSystemUIFont\";\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(232, 255, 231)\n"
"\n"
"}\n"
"QTextEdit{\n"
"	font: 18pt \".AppleSystemUIFont\";\n"
"}")
        self.layoutWidget = QWidget(Form_subprocess)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 258, 285))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.textEdit.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(Form_subprocess)

        QMetaObject.connectSlotsByName(Form_subprocess)
    # setupUi

    def retranslateUi(self, Form_subprocess):
        Form_subprocess.setWindowTitle(QCoreApplication.translate("Form_subprocess", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_subprocess", u"Subprocess:", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form_subprocess", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("Form_subprocess", u"Output:", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form_subprocess", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>", None))
    # retranslateUi

