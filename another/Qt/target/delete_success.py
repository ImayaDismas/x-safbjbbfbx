#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QLabel, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        closeButton = QPushButton("Close", self)
        closeButton.move(100, 100)
        closeButton.clicked.connect(QCoreApplication.instance().quit)

        lbl3 = QLabel('Target Deleted Successfully!!', self)
        lbl3.move(55, 50)

        self.resize(300, 150)
        self.center()
        self.setWindowTitle('Status')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
