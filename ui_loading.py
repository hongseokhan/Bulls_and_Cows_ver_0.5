# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loading.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoadingWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropshadowframe = QFrame(self.centralwidget)
        self.dropshadowframe.setObjectName(u"dropshadowframe")
        self.dropshadowframe.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(56, 58, 89);\n"
"color: rgb(220, 220, 200);\n"
"border-radius:10px;\n"
"}")
        self.dropshadowframe.setFrameShape(QFrame.StyledPanel)
        self.dropshadowframe.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropshadowframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 50, 341, 91))
        font = QFont()
        font.setFamily(u"Sans Serif")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(254,  121, 198);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.dropshadowframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 140, 341, 31))
        font1 = QFont()
        font1.setFamily(u"Sans Serif")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:rgb(98,  114, 198);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropshadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 250, 481, 20))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgb(98, 114, 164);\n"
"color:rgb(200, 200, 200);\n"
"border-style: none;\n"
"text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.54, x2:1, y2:0, stop:0.00862069 rgba(115, 210, 22, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropshadowframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 270, 341, 31))
        font2 = QFont()
        font2.setFamily(u"Sans Serif")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(211, 215, 207);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropshadowframe)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc22b\uc790\uc57c\uad6c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bulls and Cows", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"loading...", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

