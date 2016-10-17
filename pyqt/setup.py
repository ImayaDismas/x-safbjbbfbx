#!/usr/bin/python3

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
from PyQt5.QtCore import QTimer


class GateKeeper(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # start of the combo

        operator = QComboBox(self)
        operator.addItem("Operator")
        operator.addItem("Safaricom")
        operator.addItem("Airtel")
        operator.addItem("Orange")
        operator.activated[str].connect(self.changeValue)

        operator.move(250, 100)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('web.png'))
        self.label.setGeometry(10, 70, 250, 250)


        technology = QComboBox(self)
        technology.addItem("Technology")
        technology.addItem("2G")
        technology.addItem("3G")
        technology.addItem("4G")

        technology.move(250, 175)

        modem = QComboBox(self)
        modem.addItem("Modem")
        modem.addItem("Modem 1")
        modem.addItem("Modem 2")
        modem.addItem("Modem 3")
        modem.addItem("Modem 4")
        modem.addItem("Modem 5")
        modem.addItem("Modem 6")

        modem.move(250, 250)

        # combo.activated[str].connect(self.onActivated)
        # end of combo

        mode = QComboBox(self)
        mode.addItem("Mode")
        mode.addItem("Accept")
        mode.addItem("Reject")

        mode.move(420, 70)

        lac = QComboBox(self)
        lac.addItem("Lac")
        lac.addItem("1")
        lac.addItem("2")
        lac.addItem("3")
        lac.addItem("4")
        lac.addItem("5")
        lac.addItem("6")
        lac.addItem("7")
        lac.addItem("8")
        lac.addItem("9")
        lac.addItem("10")

        lac.move(420, 120)
        # lac.setGeometry(420, 120, 200, 30)

        # this is the edit text

        self.cid = QLabel("CID", self)
        self.cid.move(420, 170)
        self.cidedit = QLineEdit(self)
        # self.cidedit.move(480, 170)
        self.cidedit.setGeometry(480, 170, 150, 30)

        self.channel = QLabel("Channel", self)
        self.channel.move(420, 220)
        self.channeledit = QLineEdit(self)
        # self.channeledit.move(480, 220)
        self.channeledit.setGeometry(480, 220, 150, 30)

        # end of the edit text

        # this is the slider section
        self.pwd = QLabel("Pwd", self)
        self.pwd.move(420, 250)
        sld = QSlider(Qt.Horizontal, self)
        # sld.setFocusPolicy(Qt.NoFocus)
        sld.setFocusPolicy(Qt.StrongFocus)
        sld.setTickPosition(QSlider.TicksBothSides)
        sld.setTickInterval(2)
        sld.setRange(0,20)
        sld.setSingleStep(1)
        sld.setGeometry(420, 270, 300, 30)

        valueLabel = QLabel("Current value:")

        # end of the slider section

        btn = QPushButton('START', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(450, 350)

        stopbtn = QPushButton('STOP', self)
        stopbtn.setToolTip('This is a <b>QPushButton</b> widget')
        stopbtn.resize(stopbtn.sizeHint())
        stopbtn.move(600, 350)

        btn.clicked.connect(self.buttonClicked)
        stopbtn.clicked.connect(self.buttonClicked)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 350)

        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgb(11, 181, 255);color:white;font-weight:bold;}")
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
        if sender.text() == "START":
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,255,0);color:black;font-weight:bold;}")
            self.statusBar().showMessage('Setting up...........')
            QTimer.singleShot(3000, self.readyRunning)
        elif sender.text() == "STOP":
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:white;font-weight:bold;}")
            self.statusBar().showMessage('Stopped')
        else:
            self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,255,0);color:white;font-weight:bold;}")

        # self.statusBar().showMessage(sender.text() + ' was pressed')

    def readyRunning(self):

        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(0, 255, 0);color:white;font-weight:bold;}")
        self.statusBar().showMessage('Ready')


    # def onActivated(self, text):
    #
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()
    def changeValue(self, text):

        if text == 'Safaricom':
            self.label.setPixmap(QPixmap('safaricom.png'))
        elif text == 'Airtel':
            self.label.setPixmap(QPixmap('airtel.png'))
        elif text == 'Orange':
            self.label.setPixmap(QPixmap('orange.png'))
        else:
            self.label.setPixmap(QPixmap('web.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GateKeeper()
    sys.exit(app.exec_())
