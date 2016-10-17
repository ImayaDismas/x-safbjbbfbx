#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create three toggle buttons.
They will control the background colour of a
QFrame.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLabel, QComboBox, QLineEdit, QTextEdit, QGridLayout, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, pyqtSlot

class Window(QWidget):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        button = QPushButton(self.tr("Click me!"))

        button.clicked.connect(self.fade)

        layout = QVBoxLayout(self)
        layout.addWidget(button)

    def fade(self):

        self.setWindowOpacity(0.5)
        QTimer.singleShot(1000, self.unfade)

    def unfade(self):

        self.setWindowOpacity(1)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
