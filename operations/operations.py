# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operations.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Operations(object):
    def setupUi(self, Operations):
        Operations.setObjectName("Operations")
        Operations.resize(270, 221)
        self.centralWidget = QtWidgets.QWidget(Operations)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 251, 201))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 170, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 211, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(90, 30, 80, 22))
        self.pushButton.setObjectName("pushButton")
        Operations.setCentralWidget(self.centralWidget)

        self.retranslateUi(Operations)
        QtCore.QMetaObject.connectSlotsByName(Operations)

    def retranslateUi(self, Operations):
        _translate = QtCore.QCoreApplication.translate
        Operations.setWindowTitle(_translate("Operations", "Operations"))
        self.groupBox.setTitle(_translate("Operations", "Operations"))
        self.pushButton_2.setText(_translate("Operations", "Send"))
        self.pushButton.setText(_translate("Operations", "Call"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Operations = QtWidgets.QMainWindow()
    ui = Ui_Operations()
    ui.setupUi(Operations)
    Operations.show()
    sys.exit(app.exec_())

