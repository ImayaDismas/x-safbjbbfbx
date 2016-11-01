from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView, QApplication
import sys

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QMYSQL", "my_sql_db")
db.setHostName("localhost")
db.setDatabaseName("usrdb")
db.setUserName("usr")
db.setPassword("passwrd")
db.open()

testModel = QSqlTableModel()
testModel.setTable("test")
testModel.setEditStrategy(QSqlTableModel.OnFieldChange)
testModel.select()

testView = QTableView()
testView.setModel(testModel)

app.exec_()
