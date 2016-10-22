import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
    QSplitter, QPushButton, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


        QWidget *window = new QWidget
        QPushButton *button1 = new QPushButton("One")
        QPushButton *button2 = new QPushButton("Two")
        QPushButton *button3 = new QPushButton("Three")
        QPushButton *button4 = new QPushButton("Four")
        QPushButton *button5 = new QPushButton("Five")

        QHBoxLayout *layout = new QHBoxLayout
        layout->addWidget(button1)
        layout->addWidget(button2)
        layout->addWidget(button3)
        layout->addWidget(button4)
        layout->addWidget(button5)

        window->setLayout(layout)
        window->show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
