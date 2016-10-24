#!/usr/bin/python3

import sys
import os, errno
import configparser
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLabel, QSpinBox, QCompleter, QComboBox, QLineEdit, QTextEdit, QGridLayout, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QStringListModel

config = configparser.RawConfigParser()
config.add_section('Settings')

class Target(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        layout = QVBoxLayout()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.model = QStringListModel()
        self.model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])

        self.completer = QCompleter()
        self.completer.setModel(self.model)

        self.lineedit = QLineEdit(self)
        self.lineedit.setCompleter(self.completer)
        self.lineedit.setGeometry(50, 50, 250, 30)

        self.search = QPushButton('Search', self)
        self.search.resize(self.search.sizeHint())
        self.search.setGeometry(270, 50, 50, 30)
        layout.addWidget(self.search)


        self.add = QPushButton('ADD', self)
        self.add.resize(self.add.sizeHint())
        self.add.setGeometry(500, 50, 50, 30)
        layout.addWidget(self.add)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('web.png'))
        self.label.setGeometry(400, 120, 250, 250)
        layout.addWidget(self.label)


        self.name = QLabel("Name", self)
        self.name.move(620, 120)
        layout.addWidget(self.name)
        self.nameedit = QLineEdit(self)
        self.nameedit.setGeometry(700, 120, 150, 30)
        layout.addWidget(self.nameedit)

        self.group = QLabel("Group", self)
        self.group.move(620, 170)
        layout.addWidget(self.group)
        self.groupedit = QLineEdit(self)
        self.groupedit.setGeometry(700, 170, 150, 30)
        layout.addWidget(self.groupedit)

        self.bio = QPushButton('Bio', self)
        self.bio.resize(self.bio.sizeHint())
        self.bio.move(620, 260)
        layout.addWidget(self.bio)

        self.network = QPushButton('Network ID', self)
        self.network.resize(self.network.sizeHint())
        self.network.move(620, 300)
        layout.addWidget(self.network)

        self.notes = QPushButton('Notes', self)
        self.notes.resize(self.notes.sizeHint())
        self.notes.move(620, 340)
        layout.addWidget(self.notes)



        self.operations = QPushButton('Operations', self)
        self.operations.resize(self.operations.sizeHint())
        self.operations.move(450, 400)
        layout.addWidget(self.operations)

        self.calls = QPushButton('Calls', self)
        self.calls.resize(self.calls.sizeHint())
        self.calls.move(450, 480)
        layout.addWidget(self.calls)

        self.sms = QPushButton('Sms', self)
        self.sms.resize(self.sms.sizeHint())
        self.sms.move(450, 550)
        layout.addWidget(self.sms)

        self.qbtn = QPushButton('Quit', self)
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 550)
        layout.addWidget(self.qbtn)

        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgb(11, 181, 255);color:white;font-weight:bold;}")
        self.statusBar()


        self.resize(950, 650)
        self.center()

        # self.setLayout(layout)
        self.setWindowTitle('Target')
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






if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Target()
    sys.exit(app.exec_())
