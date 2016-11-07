# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
from PyQt5.QtCore import QCoreApplication

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(355, 497)
        AddUser.move(490, 100)
        self.centralWidget = QtWidgets.QWidget(AddUser)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 120, 201, 81))
        self.textEdit_3.setObjectName("textEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 81, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 41, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 59, 14))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 61, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 301, 451))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 310, 201, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 59, 14))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(90, 200, 201, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 130, 21, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 420, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 420, 80, 22))
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 380, 111, 22))
        self.pushButton_3.clicked.connect(lambda:self.run('image.py'))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox.raise_()
        self.textEdit_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        AddUser.setCentralWidget(self.centralWidget)

        self.retranslateUi(AddUser)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "Edit Target"))
        self.label_4.setText(_translate("AddUser", "Name:"))
        self.label_5.setText(_translate("AddUser", "Group:"))
        self.groupBox.setTitle(_translate("AddUser", "Edit Target"))
        self.label_3.setText(_translate("AddUser", "Notes:"))
        self.label_2.setText(_translate("AddUser", "Net_ID:"))
        self.label.setText(_translate("AddUser", "Bio:"))
        self.pushButton.setText(_translate("AddUser", "Save"))
        self.pushButton_2.setText(_translate("AddUser", "Cancel"))
        self.pushButton_3.setText(_translate("AddUser", "+ Change Image"))

    def run(self, path):
        subprocess.call(['python3',path])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUser = QtWidgets.QMainWindow()
    ui = Ui_AddUser()
    ui.setupUi(AddUser)
    AddUser.show()
    sys.exit(app.exec_())
