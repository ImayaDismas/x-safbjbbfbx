#!/usr/bin/env python3
import sys

from PyQt5.QtCore import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
page = QWebPage()
web_url = "https://www.google.com/"
web = QWebView()
web.load(QUrl(web_url))
web.show()

sys.exit(app.exec_())