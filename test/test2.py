#!/usr/bin/python3

import sys
import os, errno
import configparser
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLabel, QSpinBox, QComboBox, QLineEdit, QTextEdit, QGridLayout, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

config = configparser.RawConfigParser()

class GateKeeper(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        layout = QVBoxLayout()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Search Target")
        self.lineEdit.resize(250, 25)
        self.lineEdit.textChanged.connect(self.sync_listWidget)


        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgb(11, 181, 255);color:white;font-weight:bold;}")
        self.statusBar()


        self.resize(750, 450)
        self.center()

        # self.setLayout(layout)
        self.setWindowTitle('SetUp')

        self.show()

    def sync_listWidget(self, txt):
        global text
        text = txt
        config.read('target.txt')
        curr = config.get('Target', 'id')
        # print (curr)
        curre = curr.split(' ')

        print(curre[1])

        # print(txt)

    # x = sync_listWidget(self, txt)

    #print(text)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GateKeeper()
    sys.exit(app.exec_())
