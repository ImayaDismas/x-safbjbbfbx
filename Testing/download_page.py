from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication

import sys
import codecs

from gi._signalhelper import Signal


class Downloader(QObject):
    # To be emitted when every items are downloaded
    done = Signal()

    def __init__(self, urlList, parent = None):
        super(Downloader, self).__init__(parent)
        self.urlList = urlList
        self.counter = 0
        # As you probably don't need to display the page
        # you can use QWebPage instead of QWebView
        self.page = QWebPage(self)
        self.page.loadFinished.connect(self.save)
        self.startNext()

    def currentUrl(self):
        return self.urlList[self.counter][0]

    def currentFilename(self):
        return self.urlList[self.counter][1]

    def startNext(self):
        print("Downloading %s..."%self.currentUrl())
        self.page.mainFrame().load(self.currentUrl())

    def save(self, ok):
        if ok:
            data = self.page.mainFrame().toHtml()
            with codecs.open(self.currentFilename(), encoding="utf-8", mode="w") as f:
                f.write(data)
            print("Saving %s to %s."%(self.currentUrl(), self.currentFilename()))
        else:
            print("Error while downloading %s\nSkipping."%self.currentUrl())
        self.counter += 1
        if self.counter < len(self.urlList):
            self.startNext()
        else:
            self.done.emit()

urlList = [("http://news.google.com", "google.html"),
    ("http://www.stackoverflow.com","stack.html"),
    ("http://www.imdb.com", "imdb.html")]

app = QApplication(sys.argv)
downloader = Downloader(urlList)
# Quit when done
downloader.done.connect(app.quit)

# To view the pages
web = QWebView()
# To prevent user action that would interrupt the current page loading
web.setDisabled(True)
web.setPage(downloader.page)
web.show()

sys.exit(app.exec_())