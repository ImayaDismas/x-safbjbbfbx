from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import (QWidget, QApplication)
import sys
import configparser

config = configparser.RawConfigParser()
config.add_section('image_url')

def select_image_dir():
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()

    w.resize(320, 240)
    filename = QFileDialog.getOpenFileName(w, 'Select Image', '/home', "Images (*.png *.xpm *.jpg)")
    # print(filename[0])
    config.set('image_url', 'url', filename[0])

    # Writing to file 'imageurl.txt'
    with open('imageurl.txt', 'w') as configfile:
        config.write(configfile)


if __name__ == "__main__":
    import sys
    # Create an PyQT4 application object.
    app = QtWidgets.QApplication(sys.argv)
    select_image_dir()
