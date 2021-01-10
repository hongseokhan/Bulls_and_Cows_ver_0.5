# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_selectsocket.ui'
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

from ui_serverwindow import Ui_ServerWindow
from ui_clientwindow import Ui_ClientWindow

class ServerWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.server = Ui_ServerWindow()
        self.server.setupUi(self)

class ClientWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.client = Ui_ClientWindow()
        self.client.setupUi(self)
class Ui_Selectsocket(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(344, 185)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 161, 151))
        self.pushButton.clicked.connect(self.selectserver)
        font = QFont()
        font.setPointSize(21)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 20, 161, 151))
        self.pushButton_2.clicked.connect(self.selectclient)
        self.pushButton_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Server", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Client", None))
    # retranslateUi
    def selectserver(self):
        self.server = ServerWindow()
        self.server.show()
    def selectclient(self):
        self.client = ClientWindow()
        self.client.show()
