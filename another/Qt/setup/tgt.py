# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Target.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import (QCompleter)


class Ui_Target(object):
    def TargetUi(self, Target):
        Target.setObjectName("Target")

        self.model = QStringListModel()
        self.model.setStringList(['Dismas', 'Imaya', 'James', 'Pius', 'Victor'])

        self.completer = QCompleter()
        self.completer.setModel(self.model)

        Target.resize(1200, 510)
        self.centralWidget = QtWidgets.QWidget(Target)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setCompleter(self.completer)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(243, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(242, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 7, 2)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 2, 4, 2)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 4, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 5, 3, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 2)
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 6, 4, 2, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 2, 1, 2)
        Target.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(Target)
        self.statusBar.setObjectName("statusBar")
        Target.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Target)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 19))
        self.menuBar.setObjectName("menuBar")
        Target.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(Target)
        self.toolBar.setObjectName("toolBar")
        Target.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(Target)
        self.toolBar_2.setObjectName("toolBar_2")
        Target.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(Target)
        QtCore.QMetaObject.connectSlotsByName(Target)

        self.setWindowIcon(QIcon('web.png'))

    def retranslateUi(self, Target):
        _translate = QtCore.QCoreApplication.translate
        Target.setWindowTitle(_translate("Target", "Target"))
        self.pushButton.setText(_translate("Target", "ADD"))
        self.label.setText(_translate("Target", "Name"))
        self.label_2.setText(_translate("Target", "Group"))
        self.pushButton_2.setText(_translate("Target", "Bio"))
        self.pushButton_3.setText(_translate("Target", "Network ID"))
        self.pushButton_5.setText(_translate("Target", "Operations"))
        self.pushButton_4.setText(_translate("Target", "Notes"))
        self.pushButton_6.setText(_translate("Target", "Calls"))
        self.pushButton_7.setText(_translate("Target", "Sms"))
        self.toolBar.setWindowTitle(_translate("Target", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("Target", "toolBar_2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Target = QtWidgets.QMainWindow()
    ui = Ui_Target()
    ui.TargetUi(Target)
    Target.show()
    sys.exit(app.exec_())
