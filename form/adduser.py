# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QTextEdit)

class Ui_AddUser(object):
    def setupUi(self, AddUser):
        AddUser.setObjectName("AddUser")
        AddUser.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(AddUser)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 9, 245, 164))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.groupLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.groupLabel.setObjectName("groupLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.groupLabel)
        self.groupLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.groupLineEdit.setObjectName("groupLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.groupLineEdit)
        self.bioLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.bioLabel.setObjectName("bioLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bioLabel)
        self.bioLineEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.bioLineEdit.setObjectName("bioLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bioLineEdit)
        self.networkIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.networkIDLabel.setObjectName("networkIDLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.networkIDLabel)
        self.networkIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.networkIDLineEdit.setObjectName("networkIDLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.networkIDLineEdit)
        self.notesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.notesLabel.setObjectName("notesLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.notesLabel)
        self.notesLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.notesLineEdit.setObjectName("notesLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.notesLineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        AddUser.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(AddUser)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 19))
        self.menuBar.setObjectName("menuBar")
        AddUser.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(AddUser)
        self.mainToolBar.setObjectName("mainToolBar")
        AddUser.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(AddUser)
        self.statusBar.setObjectName("statusBar")
        AddUser.setStatusBar(self.statusBar)

        self.retranslateUi(AddUser)
        QtCore.QMetaObject.connectSlotsByName(AddUser)

    def retranslateUi(self, AddUser):
        _translate = QtCore.QCoreApplication.translate
        AddUser.setWindowTitle(_translate("AddUser", "AddUser"))
        self.nameLabel.setText(_translate("AddUser", "Name:"))
        self.groupLabel.setText(_translate("AddUser", "Group:"))
        self.bioLabel.setText(_translate("AddUser", "Bio:"))
        self.networkIDLabel.setText(_translate("AddUser", "Network ID:"))
        self.notesLabel.setText(_translate("AddUser", "Notes:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUser = QtWidgets.QMainWindow()
    ui = Ui_AddUser()
    ui.setupUi(AddUser)
    AddUser.show()
    sys.exit(app.exec_())

