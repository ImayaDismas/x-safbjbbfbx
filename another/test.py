import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QCompleter, QLineEdit, QVBoxLayout, QApplication)
from PyQt5.QtCore import QStringListModel

app = QApplication(sys.argv)

model = QStringListModel()
model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])

completer = QCompleter()
completer.setModel(model)

lineedit = QLineEdit()
lineedit.setCompleter(completer)
lineedit.show()

sys.exit(app.exec_())
