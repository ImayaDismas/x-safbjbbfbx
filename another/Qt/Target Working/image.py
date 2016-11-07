from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import (QWidget, QApplication)
import sys

class filedialogdemo(QWidget):
   def __init__(self):
      super(filedialogdemo, self).__init__()

      # The QWidget widget is the base class of all user interface objects in PyQt4.
      w = QWidget()

      w.resize(320, 240)
      filename = QFileDialog.getOpenFileName(w, 'Select Image', '/home', "Images (*.png *.xpm *.jpg)")
      print(filename)


app = QApplication(sys.argv)
ex = filedialogdemo()
ex.show()
sys.exit(app.exec_())
