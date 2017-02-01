import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

import utils


from PyQt5 import QtCore


class SlideShowPics(QMainWindow):

    """ SlideShowPics class defines the methods for UI and
        working logic
    """
    def __init__(self, imgLst, parent=None):
        super(SlideShowPics, self).__init__(parent)
        # self._path = path
        self._imageCache = []
        self._imagesInList = imgLst
        self._pause = False
        self._count = 0
        self.animFlag = True
        self.updateTimer = QTimer()
        # self.connect(self.updateTimer, pyqtSignal("timeout()"), self.nextImage)
        self.prepairWindow()
        self.nextImage()

    def prepairWindow(self):
        # Centre UI
        screen = QDesktopWidget().screenGeometry(self)
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        self.setStyleSheet("QWidget{background-color: #000000;}")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.buildUi()

        self.playPause()

    def buildUi(self):
        self.label = QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def nextImage(self):
        """ switch to next image or previous image
        """
        if self._imagesInList:
            if self._count == len(self._imagesInList):
                self._count = 0

            self.showImageByPath(
                    self._imagesInList[self._count])

            if self.animFlag:
                self._count += 1
            else:
                self._count -= 1


    def showImageByPath(self, path):
        if path:
            image = QImage(path)
            pp = QPixmap.fromImage(image)
            self.label.setPixmap(pp.scaled(
                    self.label.size(),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation))

    def playPause(self):
        if not self._pause:
            self._pause = True
            self.updateTimer.start(2500)
            return self._pause
        else:
            self._pause = False
            self.updateTimer.stop()

    def keyPressEvent(self, keyevent):
        """ Capture key to exit, next image, previous image,
            on Escape , Key Right and key left respectively.
        """
        event = keyevent.key()
        if event == Qt.Key_Escape:
            self.close()
        if event == Qt.Key_Left:
            self.animFlag = False
            self.nextImage()
        if event == Qt.Key_Right:
            self.animFlag = True
            self.nextImage()
        if event == 32:
            self._pause = self.playPause()

def main(paths):
    if isinstance(paths, list):
        imgLst = utils.imageFilePaths(paths)
    elif isinstance(paths, str):
        imgLst =  utils.imageFilePaths([paths])
    else:
        print("You can either enter a list of paths or single path")
    app = QtWidgets.QApplication(sys.argv)
    if imgLst:
        window =  SlideShowPics(imgLst)
        window.show()
        window.raise_()
        app.exec_()
    else:
        msgBox = QMessageBox()
        msgBox.setText("No Image found in any of the paths below\n\n%s" % paths)
        msgBox.setStandardButtons(msgBox.Cancel | msgBox.Open);
        if msgBox.exec_() == msgBox.Open:
            main(str(QFileDialog.getExistingDirectory(None,
                "Select Directory to SlideShow",
                os.getcwd())))

if __name__ == '__main__':
    curntPaths = os.getcwd()
    if len(sys.argv) > 1:
        curntPaths = sys.argv[1:]
    main(curntPaths)