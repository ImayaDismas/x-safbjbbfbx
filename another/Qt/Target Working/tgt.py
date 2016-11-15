#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Target.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import configparser
from time import gmtime, strftime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import (QCompleter, QPushButton, QLabel, QDesktopWidget)
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import subprocess
import MySQLdb
from PIL.ImageQt import ImageQt
from PIL import Image
import requests
import io
import os
from io import StringIO

configt = configparser.RawConfigParser()
config = configparser.RawConfigParser()
configt.add_section('Target')
config.add_section('List')

class Ui_Target(object):

    def TargetUi(self, Target):
        Target.setObjectName("Target")
        Target.setWindowIcon(QIcon('web.png'))

        self.model = QStringListModel()
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()
        conn.close()
        #     item = QtWidgets.QListWidgetItem("Target %i" % i)
        #     self.listWidget.addItem(item)
        self.model.setStringList(my_target)

        self.completer = QCompleter()
        self.completer.setModel(self.model)

        # Target.resize(1200, 510)
        Target.showMaximized()
        self.centralWidget = QtWidgets.QWidget(Target)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")

        # self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        # self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Search Target")
        self.lineEdit.setCompleter(self.completer)
        self.lineEdit.resize(250, 25)
        self.lineEdit.move(100, 55)
        self.lineEdit.textChanged.connect(self.sync_listWidget)
        self.lineEdit.textChanged.connect(self.load_image_search)
        # self.lineEdit.textChanged.connect(self.NetworkIdButtonSearch)
        # self.lineEdit.setEnabled(True)
        # self.lineEdit.raise_()

        # self.gridLayout.addWidget(self.lineEdit1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(243, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.run('adduser.py'))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)


        spacerItem1 = QtWidgets.QSpacerItem(242, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 2, 1)

        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        for i in my_target:
            # item = QtWidgets.QListWidgetItem("Target %i" % i)
            # item.setTextAlignment(Qt.AlignHCenter)
            self.listWidget.addItem(i)

        # self.currentItemChanged.connect(print_info)

        self.listWidget.currentItemChanged.connect(self.print_info)
        self.listWidget.currentItemChanged.connect(self.NetworkIdButton)
        self.listWidget.currentItemChanged.connect(self.NotesButton)
        self.listWidget.currentItemChanged.connect(self.BioButton)
        self.listWidget.currentItemChanged.connect(self.load_image)

        # x = self.print_info.target_txt
        # print(x)
        # self.line = QtWidgets.QLineEdit(self.centralWidget)
        # words = self.line.text()
        # print(words)

        self.gridLayout.addWidget(self.listWidget, 1, 0, 7, 2)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")


        self.scene =QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0,0,0,0)
        self.scene.addPixmap(QPixmap('web.png'))
        self.graphicsView.setScene(self.scene)

        self.gridLayout.addWidget(self.graphicsView, 1, 2, 4, 2)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 4, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 5, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 5, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.BioButton)
        self.pushButton_2.clicked.connect(self.BioButtonSearch)
        self.gridLayout.addWidget(self.pushButton_2, 3, 4, 1, 1)


        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setText('My name is Cecil Lewis, and I am a survivor.  For weeks I daydreamed of my family’s vacation to Thailand.  That vacation was a much needed time away from my hectic hours as a lawyer in a medium-sized firm in Chicago.  But as it turned out my time there was not relaxing at all, life had a different plan.  While on that vacation, our hotel received word of a devastating tsunami set to hit land, we were to evacuate quickly.  Lucky for my family we were further uphill hiking that day when we heard the news. We left to find an even safer location just before the water came on shore. We survived the tsunami. It was an act of God. When we returned many days later we found our resort was no more.')
        self.gridLayout.addWidget(self.textBrowser, 3, 5, 3, 1)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 4, 1, 1)
        self.pushButton_3.clicked.connect(self.NetworkIdButton)
        self.pushButton_3.clicked.connect(self.NetworkIdButtonSearch)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:self.run('operations.py'))
        # self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 2)
        self.pushButton_5.resize(250, 25)
        self.pushButton_5.move(540, 455)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 4, 1, 1)
        self.pushButton_4.clicked.connect(self.NotesButton)
        self.pushButton_4.clicked.connect(self.NotesButtonSearch)


        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 2)
        self.pushButton_6.clicked.connect(self.CallsButton)
        # self.pushButton_6.resize(250, 25)
        # self.pushButton_6.move(540, 455)

        self.listWidget_1 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_1.setObjectName("listWidget_1")
        self.gridLayout.addWidget(self.listWidget_1, 6, 4, 2, 2)

        self.listWidget_1 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_1.setObjectName("listWidget_1")
        self.gridLayout.addWidget(self.listWidget_1, 6, 4, 2, 2)


        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 2, 1, 2)
        self.pushButton_7.clicked.connect(self.SmsButton)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda:self.run('edituser.py'))
        self.pushButton_8.move(500, 405)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda:self.run('areyousure.py'))
        self.pushButton_9.move(720, 405)

        Target.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(Target)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.setStyleSheet("QStatusBar{padding-left:8px;background:rgb(11, 181, 255);color:white;font-weight:bold;}")
        self.StatusMsg()
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

    def print_info(self):
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.listWidget.currentItem().text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')



        curs = conn.cursor()

        # curs.execute("SELECT * FROM users where id = %i" %int(curre[1]))
        curs.execute("SELECT * FROM users where id = %i" %int(curre))
        row = curs.fetchone()
        while row is not None:
            # self.line.setText(target_txt)
            self.lineEdit_2.setText(row[1])
            self.lineEdit_3.setText(row[2])
            row = curs.fetchone()
        curs.close()
        conn.close()




    def BioButton(self):
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.listWidget.currentItem().text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        curs = conn.cursor()

        curs.execute("SELECT * FROM users where id = %i" %int(curre))
        row = curs.fetchone()
        while row is not None:
            self.textBrowser.setText(row[3])
            row = curs.fetchone()
        curs.close()
        conn.close()

    def NetworkIdButton(self):
        # curr = self.listWidget.currentItem().text()
        #
        # curre = curr.split(' ')
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.listWidget.currentItem().text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        curs = conn.cursor()

        curs.execute("SELECT * FROM users where id = %i" %int(curre))
        row = curs.fetchone()
        while row is not None:
            self.textBrowser.setText(row[4])
            row = curs.fetchone()
        curs.close()
        conn.close()


    def NotesButton(self):
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.listWidget.currentItem().text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        curs = conn.cursor()

        curs.execute("SELECT * FROM users where id = %i" %int(curre))
        row = curs.fetchone()
        while row is not None:
            self.textBrowser.setText(row[5])
            row = curs.fetchone()
        curs.close()
        conn.close()



    def load_image(self):

        self.scene.clear()
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.listWidget.currentItem().text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        filename = "/home/imaya/Documents/Projects/x-safbjbbfbx/another/Qt/Target Working/images/*"

        query = ("SELECT images FROM users where id = %i" %int(curre))

        try:
            # query blob data form the users table
            cursor = conn.cursor()
            cursor.execute(query,)
            photo = cursor.fetchone()[0]

            # write blob data into a file
            def write_file(data, filename):
                with open(filename, 'wb') as f:
                    f.write(data)

            write_file(photo, filename)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

        self.scene.addPixmap(QPixmap('images/*'))
        # conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        # curs = conn.cursor()
        #
        # curs.execute("SELECT * FROM users where id = %i" %int(curre[1]))
        # row = curs.fetchone()
        # while row is not None:
        #     url = row[6]
        #     response = requests.get(url)
        #     # img = Image.open(io.BytesIO(response.content))
        #     qimage = ImageQt(response.content)
        #     # qimage = ImageQt(img)
        #     pixmap = QtGui.QPixmap.fromImage(qimage)
        #     self.scene.addPixmap(QPixmap(pixmap))
        #     row = curs.fetchone()
        # curs.close()
        # conn.close()

    def load_image_search(self, text):

        self.scene.clear()
        # curre = text.split(' ')

        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = text
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        filename = "/home/imaya/Documents/Projects/x-safbjbbfbx/another/Qt/Target Working/images/*"

        query = ("SELECT images FROM users where id = %i" %int(curre))

        try:
            # query blob data form the users table
            cursor = conn.cursor()
            cursor.execute(query,)
            photo = cursor.fetchone()[0]

            # write blob data into a file
            def write_file(data, filename):
                with open(filename, 'wb') as f:
                    f.write(data)

            write_file(photo, filename)

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

        self.scene.addPixmap(QPixmap('images/*'))


    def sync_listWidget(self, text):

        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = text
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        # target_id = text.split(' ')
        # target_txt = str(target_id[1])
        #
        # # print(target_txt)
        # config.set('Target', 'id', text)
        #
        # # Writing to file 'target.txt'
        # with open('target.txt', 'w') as configfile:
        #     config.write(configfile)
        # # print(target_id[1])

        cur1 = conn.cursor()

        cur1.execute("SELECT * FROM users where id = %i" %int(curre))
        row = cur1.fetchone()
        while row is not None:
            # print (row[0],row[1],row[2],row[3],row[4])
            self.lineEdit_2.setText(row[1])
            self.lineEdit_3.setText(row[2])
            row = cur1.fetchone()
        cur1.close()

        cur2 = conn.cursor()
        cur2.execute("SELECT * FROM users where id = %i" %int(curre))
        row = cur2.fetchone()
        while row is not None:
            self.textBrowser.setText(row[3])
            row = cur2.fetchone()
        cur2.close()

        conn.close()



    def BioButtonSearch(self):

        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.lineEdit.text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        cur2 = conn.cursor()
        cur2.execute("SELECT * FROM users where id = %i" %int(curre))
        row = cur2.fetchone()
        while row is not None:
            self.textBrowser.setText(row[3])
            row = cur2.fetchone()
        cur2.close()
        conn.close()

    def NetworkIdButtonSearch(self):
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.lineEdit.text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        cur3 = conn.cursor()
        cur3.execute("SELECT * FROM users where id = %i" %int(curre))
        row = cur3.fetchone()
        while row is not None:
            self.textBrowser.setText(row[4])
            row = cur3.fetchone()
        cur3.close()
        conn.close()

    def NotesButtonSearch(self):
        conn = MySQLdb.connect(user="root", passwd="nairobi2013", db="data_target")
        cur = conn.cursor()

        status = 1
        cur.execute("SELECT * FROM users where target_status = %i" %status)
        row = cur.fetchone()
        my_target_name = []
        my_target_id = []
        while row is not None:
            # my_target.append("Target %i" % row[0] + " %s" %row[1])
            my_target_id.append("%i" %row[0])
            my_target_name.append("%s" %row[1])
            row = cur.fetchone()
        cur.close()

        curr = self.lineEdit.text()
        for i in my_target_name:
            if curr == i:
                x = my_target_name.index(i)
                config.set('List', 'index', x)

                with open('index.txt', 'w') as configfile:
                    config.write(configfile)

        config.read('index.txt')
        index = config.get('List', 'index')

        for i in my_target_id:
            j = my_target_id.index(i)
            if index == str(j):

                value = my_target_id[j]

                configt.set('Target', 'id', value)

                with open('target.txt', 'w') as configfile:
                    configt.write(configfile)

        configt.read('index.txt')
        curre = configt.get('Target', 'id')

        cur4 = conn.cursor()
        cur4.execute("SELECT * FROM users where id = %i" %int(curre))
        row = cur4.fetchone()
        while row is not None:
            self.textBrowser.setText(row[5])
            row = cur4.fetchone()
        cur4.close()

        conn.close()


    def CallsButton(self):
        self.listWidget_1.clear()
        calls = ['0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22', '0700415505, Received, 09:22']
        for item in calls:
            self.listWidget_1.addItem(item)

    def SmsButton(self):
        self.listWidget_1.clear()
        items = ['Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.', 'Think about ways you can tell your story in a unique, unexpected way to really draw the readers in.']
        for i in items:
            self.listWidget_1.addItem(i)

    def StatusMsg(self):
        # date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        date_time = strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar.showMessage('STAT: Last seen Embakasi on '+ date_time)

    def run(self, path):
        subprocess.call(['python3',path])

    def retranslateUi(self, Target):
        _translate = QtCore.QCoreApplication.translate
        Target.setWindowTitle(_translate("Target", "Target"))
        self.pushButton.setText(_translate("Target", "ADD"))
        self.label.setText(_translate("Target", "Name"))
        self.label_2.setText(_translate("Target", "Group"))
        self.label_3.setText(_translate("Target", "Target List"))
        self.pushButton_2.setText(_translate("Target", "Bio"))
        self.pushButton_3.setText(_translate("Target", "Network ID"))
        self.pushButton_5.setText(_translate("Target", "Operations"))
        self.pushButton_4.setText(_translate("Target", "Notes"))
        self.pushButton_6.setText(_translate("Target", "Calls"))
        self.pushButton_7.setText(_translate("Target", "Sms"))
        self.pushButton_8.setText(_translate("Target", "Edit"))
        self.pushButton_9.setText(_translate("Target", "Delete"))
        self.toolBar.setWindowTitle(_translate("Target", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("Target", "toolBar_2"))

    # value_choice(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Target = QtWidgets.QMainWindow()
    ui = Ui_Target()
    ui.TargetUi(Target)
    # ui.value_choice(Target)
    Target.show()
    sys.exit(app.exec_())
