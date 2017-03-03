import os

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QWidget


class MyQTreeView(QTreeView):

    def __init__(self, path, parent=None):
        super(MyQTreeView, self).__init__(parent)

        ppath = os.path.dirname(path) # parent of path
        self.setFrameStyle(0)

        #---- File System Model ----

        sourceModel = QFileSystemModel()
        sourceModel.setRootPath(ppath)

        #---- Filter Proxy Model ----

        proxyModel = MyQSortFilterProxyModel(path)
        proxyModel.setSourceModel(sourceModel)

        #---- Filter Proxy Model ----

        self.setModel(proxyModel)
        self.setHeaderHidden(True)
        self.setRootIndex(proxyModel.mapFromSource(sourceModel.index(ppath)))

        #--- Hide All Header Sections Except First ----

        header = self.header()
        for sec in range(1, header.count()):
            header.setSectionHidden(sec, True)

    def sizeHint(self):
        baseSize = super(MyQTreeView,self).sizeHint()

        #---- get model index of "path" ----
        qindx = self.rootIndex().child(0, 0)

        if self.isExpanded(qindx): # default baseSize height will be used
            pass

        else:  # shrink baseShize height to the height of the row
            baseSize.setHeight(self.rowHeight(qindx))

        return baseSize


class MyQSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, path, parent=None):
        super(MyQSortFilterProxyModel, self).__init__(parent)

        self.path = path

    def filterAcceptsRow(self, row, parent):

        model = self.sourceModel()
        path_dta = model.index(self.path).data()
        ppath_dta = model.index(os.path.dirname(self.path)).data()

        if parent.data() == ppath_dta:
            if parent.child(row, 0).data() == path_dta:
                return True
            else:
                return False
        else:
            return True

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        super(MyTableModel, self).__init__(parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent=QModelIndex()):
        return len(self.mylist)

    def columnCount(self, parent=QModelIndex()):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

class MyDelegate(QItemDelegate):

    treeViewHeightChanged = pyqtSignal(QWidget)

    def createEditor(self, parent, option, index):

        editor = MyQTreeView(index.data(), parent)
        editor.collapsed.connect(self.sizeChanged)
        editor.expanded.connect(self.sizeChanged)

        return editor

    def sizeChanged(self):
        self.treeViewHeightChanged.emit(self.sender())

class MyTableView(QTableView):
    def __init__(self, data_list, header, *args):
        super(MyTableView, self).__init__(*args)

        #---- set up model ----

        model = MyTableModel(self, data_list, header)
        self.setModel(model)

        #---- set up delegate in last column ----

        delegate = MyDelegate()

        self.setItemDelegateForColumn(3, delegate)
        for row in range(model.rowCount()):
            self.openPersistentEditor(model.index(row, 3))

        #---- set up font and resize calls ----

        self.setFont(QFont("Courier New", 14))
        self.resizeColumnsToContents()
        delegate.treeViewHeightChanged.connect(self.resizeRowsToContents)

if __name__ == '__main__':

    header = ['Name', ' Email', ' Status', ' Path']
    data_list = [('option_A', 'zyro@email.com', 'Not Copied', '/opt'),
                 ('option_B', 'zyro@email.com', 'Not Copied', '/usr')]

    app = QApplication([])
    win = MyTableView(data_list, header)
    win.setGeometry(300, 200, 570, 450)
    win.show()
    app.exec_()