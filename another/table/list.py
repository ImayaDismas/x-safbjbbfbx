import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPlainTextEdit, QScrollArea, QApplication)


app = QtWidgets.QApplication(sys.argv)

listWidget = QtWidgets.QListWidget()       


for i in range(1,11):
    item = QtWidgets.QListWidgetItem("TGT %i" % i)
    item.setTextAlignment(Qt.AlignHCenter)
    listWidget.addItem(item)

listWidget.show()
sys.exit(app.exec_())
