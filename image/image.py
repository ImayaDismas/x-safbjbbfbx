# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import (QWidget, QApplication)
import sys

class Ui_Image(object):
    def setupUi(self, Image):
        Image.setObjectName("Image")
        Image.resize(400, 300)
        Image.move(400, 300)
        self.centralWidget = QtWidgets.QWidget(Image)
        self.centralWidget.setObjectName("centralWidget")
        Image.setCentralWidget(self.centralWidget)

        # The QWidget widget is the base class of all user interface objects in PyQt4.
        # w = QWidget()
        #
        # w.resize(320, 240)
        filename = QFileDialog.getOpenFileName(Image, 'Select Image', '/home', "Images (*.png *.xpm *.jpg)")
        print(filename)

        self.retranslateUi(Image)
        QtCore.QMetaObject.connectSlotsByName(Image)

    def retranslateUi(self, Image):
        _translate = QtCore.QCoreApplication.translate
        Image.setWindowTitle(_translate("Image", "Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image = QtWidgets.QMainWindow()
    ui = Ui_Image()
    ui.setupUi(Image)
    Image.show()
    sys.exit(app.exec_())
