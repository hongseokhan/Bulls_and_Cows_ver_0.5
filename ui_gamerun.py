# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gamerun.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_pvegame import Ui_PvegameWindow
from ui_selectsocket import Ui_Selectsocket

class PvegameWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.pvegame = Ui_PvegameWindow()
        self.pvegame.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class SelectSocketWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.selectsocket = Ui_Selectsocket()
        self.selectsocket.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class Ui_GamerunWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 741, 551))
        self.label.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.label.setPixmap(QPixmap(u"../\ub2e4\uc6b4\ub85c\ub4dc/stadium.jpg"))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 290, 551, 61))
        self.pushButton.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 215, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 italic 12pt \"Serif\";")
        self.pushButton.clicked.connect(self.start_pvegame)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 380, 551, 61))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 215, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 italic 12pt \"Serif\";")
        self.pushButton_2.clicked.connect(self.start_pvpgame)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 470, 255, 61))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 215, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 italic 12pt \"Serif\";")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 470, 255, 61))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(211, 215, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 italic 12pt \"Serif\";")
        self.pushButton_3.clicked.connect(QCoreApplication.instance().quit)
        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Player VS  Com", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Player VS Player", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
    def start_pvegame(self):
        self.ui = PvegameWindow()
        self.ui.show()
    
    def start_pvpgame(self):
        self.ui = SelectSocketWindow()
        self.ui.show()
    
    def exit(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())
