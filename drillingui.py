# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drilling.ui'
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
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(397, 850)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QPushButton{\n"
"\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 326, 611))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 216))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 63))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.layoutWidget.setPalette(palette)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(232, 255, 231, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush3)
        brush4 = QBrush(QColor(245, 245, 245, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        brush5 = QBrush(QColor(191, 191, 191, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush5)
        brush6 = QBrush(QColor(169, 169, 169, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(165, 205, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush9 = QBrush(QColor(9, 79, 209, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush9)
        brush10 = QBrush(QColor(255, 0, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.LinkVisited, brush10)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.NoRole, brush11)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        brush12 = QBrush(QColor(212, 212, 212, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        brush13 = QBrush(QColor(0, 0, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.NoRole, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush4)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.NoRole, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.pushButton.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_2.setPalette(palette2)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        palette3 = QPalette()
        brush16 = QBrush(QColor(227, 255, 231, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        self.pushButton_3.setPalette(palette3)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color:#E3FFE7;\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_4.setPalette(palette4)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(232, 255, 231);\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_5.setPalette(palette5)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(232, 255, 231);\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_6.setPalette(palette6)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(232, 255, 231);\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_7.setPalette(palette7)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(232, 255, 231);\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.pushButton_8.setPalette(palette8)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(232, 255, 231);\n"
"	font: 20pt \".AppleSystemUIFont\";\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Drilling Drone Initialization", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"MAVROS", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Vicon_bridge", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Talker (convert to pose for MAVROS)", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Drone Position Setpoint (mode 123)", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PID for Drone Position Control", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Drill Press Sensor", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Lock or Release (downward)?", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"ROS Bag", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Initialization notes:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(1) mavros should show PX4 version number;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(2) Vicon_bridge should show drilling5 published;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(6) Check DrillPress sense sho"
                        "ws D_Pos not &quot;0&quot;;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check flight mode settings in QGroundControl.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Operation processure:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Type &quot;1&quot; in window (4) to send position setpoint;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Arm drone from RC and switch to offboard mode to let drone fly to waypoint 1;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Type &quot;1&quot; in window (7) to release drill (downward);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Check &quot;Raw&quot; value from window (6) and type rounded absolute &quot;Raw&quot; value into window (7) to set offset value in release mode;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. Raise drill press;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6. In window (4), type &quot;2&quot; and press &quot;Enter&quot; to let drone fly to position 2 which is just above the board;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7. Use drill press to drill and lift afterward;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8. In window (4), type &quot;3&quot; and press &quot;Enter&quot; to let drone fly to position 3 which is above"
                        " the takeoff position;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9. In window (7), type &quot;2&quot; to lock the drill (forward);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10. Make sure RC throttle is at middle position;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11. Turn off off-board mode to switch back to &quot;position&quot; mode;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12. Manual land the drone;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13. Disarm or kill the drone.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

