from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import (QWidget, QApplication)
import sys

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

w.resize(320, 240)
filename = QFileDialog.getOpenFileName(w, 'Select Image', '/home', "Images (*.png *.xpm *.jpg)")
print(filename)

sys.exit(a.exec_())
