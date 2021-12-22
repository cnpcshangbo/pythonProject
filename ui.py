# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 473)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(255, 218, 187)\n"
"}")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 20, 421, 411))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777000, 16777000))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_connect = QPushButton(self.layoutWidget)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        self.pushButton_connect.setMinimumSize(QSize(200, 100))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        self.pushButton_connect.setFont(font1)
        self.pushButton_connect.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(255, 218, 187)\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_connect)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Serial CMDs", None))
        self.pushButton_connect.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Messages.", None))
    # retranslateUi

