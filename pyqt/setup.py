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
config.add_section('Settings')

class GateKeeper(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        layout = QVBoxLayout()

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # start of the combo

        self.operator = QComboBox(self)
        self.operator.addItem("Operator")
        self.operator.addItem("Safaricom")
        self.operator.addItem("Airtel")
        self.operator.addItem("Orange")
        self.operator.activated[str].connect(self.changeValue)

        self.operator.move(250, 100)
        layout.addWidget(self.operator)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('web.png'))
        self.label.setGeometry(10, 70, 250, 250)
        layout.addWidget(self.label)

        self.technology = QComboBox(self)
        self.technology.addItem("Technology")
        self.technology.addItem("2G")
        self.technology.addItem("3G")
        self.technology.addItem("4G")
        self.technology.activated[str].connect(self.techValue)

        self.technology.move(250, 175)
        layout.addWidget(self.technology)

        self.modem = QComboBox(self)
        self.modem.addItem("Modem")
        self.modem.addItem("Modem 1")
        self.modem.addItem("Modem 2")
        self.modem.addItem("Modem 3")
        self.modem.addItem("Modem 4")
        self.modem.addItem("Modem 5")
        self.modem.addItem("Modem 6")
        self.modem.activated[str].connect(self.modemValue)

        self.modem.move(250, 250)
        layout.addWidget(self.modem)

        # combo.activated[str].connect(self.onActivated)
        # end of combo

        self.mode = QComboBox(self)
        self.mode.addItem("Mode")
        self.mode.addItem("Accept")
        self.mode.addItem("Reject")
        self.mode.activated[str].connect(self.modeValue)

        self.mode.move(420, 70)
        layout.addWidget(self.mode)

        self.lac = QComboBox(self)
        self.lac.addItem("Lac")
        self.lac.addItem("1")
        self.lac.addItem("2")
        self.lac.addItem("3")
        self.lac.addItem("4")
        self.lac.addItem("5")
        self.lac.addItem("6")
        self.lac.addItem("7")
        self.lac.addItem("8")
        self.lac.addItem("9")
        self.lac.addItem("10")
        self.lac.activated[str].connect(self.lacValue)

        self.lac.move(420, 120)
        layout.addWidget(self.lac)
        # lac.setGeometry(420, 120, 200, 30)

        # this is the edit text

        self.cid = QLabel("CID", self)
        self.cid.move(420, 170)
        layout.addWidget(self.cid)
        self.cidedit = QLineEdit(self)
        # self.cidedit.move(480, 170)
        self.cidedit.textChanged[str].connect(self.cidChanged)
        self.cidedit.setGeometry(480, 170, 150, 30)
        layout.addWidget(self.cidedit)

        self.channel = QLabel("Channel", self)
        self.channel.move(420, 220)
        layout.addWidget(self.channel)
        self.channeledit = QLineEdit(self)
        # self.channeledit.move(480, 220)
        self.channeledit.textChanged[str].connect(self.channelChanged)
        self.channeledit.setGeometry(480, 220, 150, 30)
        layout.addWidget(self.channeledit)

        # end of the edit text

        # this is the slider section
        self.pwd = QLabel("Pwr", self)
        self.pwd.move(420, 250)
        layout.addWidget(self.pwd)

        self.valueSpinBox = QSpinBox(self)

        self.sld = QSlider(Qt.Horizontal, self)
        # sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setFocusPolicy(Qt.StrongFocus)
        self.sld.setTickPosition(QSlider.TicksBothSides)
        self.sld.setTickInterval(2)
        self.sld.setRange(0,20)
        self.sld.setSingleStep(1)
        self.sld.setGeometry(420, 270, 300, 30)
        self.sld.valueChanged[int].connect(self.sliderValue)
        self.sld.valueChanged.connect(self.valueSpinBox.setValue)
        layout.addWidget(self.sld)

        self.valueLabel = QLabel("Pwd value:", self)
        self.valueLabel.move(420, 300)
        layout.addWidget(self.valueLabel)



        self.valueSpinBox.move(500, 300)
        self.valueSpinBox.setRange(0, 20)
        self.valueSpinBox.setSingleStep(1)
        self.valueSpinBox.setValue(0)
        self.valueSpinBox.valueChanged.connect(self.sld.setValue)
        layout.addWidget(self.valueSpinBox)

        # end of the slider section

        self.btn = QPushButton('START', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(450, 350)
        self.btn.clicked.connect(self.buttonClicked)
        layout.addWidget(self.btn)

        self.stopbtn = QPushButton('STOP', self)
        self.stopbtn.setToolTip('This is a <b>QPushButton</b> widget')
        self.stopbtn.resize(self.stopbtn.sizeHint())
        self.stopbtn.move(600, 350)
        self.stopbtn.clicked.connect(self.buttonClicked)
        layout.addWidget(self.stopbtn)

        self.qbtn = QPushButton('Quit', self)
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 350)
        layout.addWidget(self.qbtn)

        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgb(11, 181, 255);color:white;font-weight:bold;}")
        self.statusBar()


        self.resize(750, 450)
        self.center()

        # self.setLayout(layout)
        self.setWindowTitle('SetUp')
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
        if sender.text() == "START":
            # Writing our configuration file to 'settings.config'
            with open('settings.config', 'w') as configfile:
                config.write(configfile)
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,255,0);color:black;font-weight:bold;}")
            self.statusBar().showMessage('Setting up...........')
            QTimer.singleShot(3000, self.readyRunning)
        elif sender.text() == "STOP":
            open('settings.config', 'w')
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:white;font-weight:bold;}")
            self.statusBar().showMessage('Stopped')
        else:
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,255,0);color:white;font-weight:bold;}")

        # self.statusBar().showMessage(sender.text() + ' was pressed')

    def readyRunning(self):

        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(0, 255, 0);color:white;font-weight:bold;}")
        self.statusBar().showMessage('Ready')


    def techValue(self, text):

        config.set('Settings', 'Technology', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def modemValue(self, text):

        config.set('Settings', 'Modem', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def modeValue(self, text):

        config.set('Settings', 'Mode', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def lacValue(self, text):

        config.set('Settings', 'Lac', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def sliderValue(self, value):

        config.set('Settings', 'PWD', value)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def cidChanged(self, text):

        config.set('Settings', 'CID', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def channelChanged(self, text):

        config.set('Settings', 'Channel', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

    def changeValue(self, text):

        config.set('Settings', 'Operator', text)

        # # Writing our configuration file to 'settings.config'
        # with open('settings.config', 'w') as configfile:
        #     config.write(configfile)

        if text == 'Safaricom':
            self.label.setPixmap(QPixmap('safaricom.png'))
        elif text == 'Airtel':
            self.label.setPixmap(QPixmap('airtel.png'))
        elif text == 'Orange':
            self.label.setPixmap(QPixmap('orange.png'))
        else:
            self.label.setPixmap(QPixmap('web.png'))

    def setValue(self, value):
        self.sld.setValue(value)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GateKeeper()
    sys.exit(app.exec_())
