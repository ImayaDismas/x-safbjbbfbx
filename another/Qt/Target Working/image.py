from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import (QWidget, QApplication)
import sys

def select_image_dir():
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()

    w.resize(320, 240)
    filename = QFileDialog.getOpenFileName(w, 'Select Image', '/home', "Images (*.png *.xpm *.jpg)")
    print(filename)


if __name__ == "__main__":
    import sys
    # Create an PyQT4 application object.
    app = QtWidgets.QApplication(sys.argv)
    select_image_dir()
