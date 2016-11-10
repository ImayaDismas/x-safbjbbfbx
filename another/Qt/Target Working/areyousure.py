#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QCoreApplication
import subprocess
from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QLabel, QApplication)
import MySQLdb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        closeButton = QPushButton("No", self)
        closeButton.move(50, 100)
        closeButton.clicked.connect(QCoreApplication.instance().quit)

        deleteButton = QPushButton("Yes", self)
        deleteButton.move(260, 100)
        deleteButton.clicked.connect(self.DeleteButton)
        deleteButton.clicked.connect(lambda:self.run('delete_success.py'))
        deleteButton.clicked.connect(QCoreApplication.instance().quit)

        lbl3 = QLabel('Are you sure you want to DELETE this Target?', self)
        lbl3.move(55, 50)

        # self.setGeometry(500, 500, 300, 150)
        self.resize(400, 150)
        self.center()
        self.setWindowTitle('Status')
        self.show()


    def DeleteButton(self):
        # curr = self.listWidget.currentItem().text()
        curr = 'Target 2'
        # print (curr)
        curre = curr.split(' ')

        # target_name = self.lineEdit_2.text()
        # print(target_name)
        # target_group = self.lineEdit.text()
        # print(target_group)
        # bio = self.textEdit_3.toPlainText()
        # print(bio)
        # network_id = self.textEdit.toPlainText()
        # print(network_id)
        # notes = self.textEdit_2.toPlainText()
        # print(notes)

        target_status = 0

        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        curs = conn.cursor()

        query = "UPDATE users SET target_status = %s WHERE id = %s"

        args = (target_status,  curre[1])

        curs.execute(query, args)
        conn.commit()
        curs.close()

        conn.close()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def run(self, path):
        subprocess.call(['python3',path])


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
