#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('START', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(450, 400)

        stopbtn = QPushButton('STOP', self)
        stopbtn.setToolTip('This is a <b>QPushButton</b> widget')
        stopbtn.resize(stopbtn.sizeHint())
        stopbtn.move(600, 400)

        btn.clicked.connect(self.buttonClicked)
        stopbtn.clicked.connect(self.buttonClicked)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 400)

        self.statusBar()

        self.resize(750, 450)
        self.center()

        self.setWindowTitle('Gate Keeper')
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
