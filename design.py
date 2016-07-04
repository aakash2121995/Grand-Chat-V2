# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created: Mon May  2 19:48:25 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1098, 808)
        MainWindow.setMaximumSize(QtCore.QSize(1098, 808))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.send = QtGui.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(880, 690, 131, 31))
        self.send.setObjectName(_fromUtf8("send"))
        self.message = QtGui.QLineEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(90, 690, 741, 27))
        self.message.setObjectName(_fromUtf8("message"))
        self.ChatWindow = QtGui.QTextBrowser(self.centralwidget)
        self.ChatWindow.setGeometry(QtCore.QRect(85, 31, 921, 591))
        self.ChatWindow.setObjectName(_fromUtf8("ChatWindow"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Grand Chat", None))
        self.send.setText(_translate("MainWindow", "Send", None))

