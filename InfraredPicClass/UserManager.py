# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import qdarkstyle
from PyQt5.QtSql import *
from addImageLibDillog import Ui_Form_addImage
from register import Ui_Form_registe


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 610)
        Form.setAutoFillBackground(False)

        # 查询模型
        self.queryModel = None
        self.queryTableModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10

        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

        # Hlayout1控件的初始化
        self.searchEdit = QLineEdit()
        self.searchEdit.setFixedHeight(32)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询")
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)
        self.searchButton.setIcon(QIcon(QPixmap("icon/search.png")))

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)

        # Hlayout2初始化
        self.jumpToLabel = QLabel("跳转到第")
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(30)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToButton = QPushButton("跳转")
        self.prevButton = QPushButton("前一页")
        self.prevButton.setFixedWidth(60)
        self.backButton = QPushButton("后一页")
        self.backButton.setFixedWidth(60)
        self.addButton = QPushButton("添加")
        self.addButton.setFixedWidth(60)
        self.deleteButton = QPushButton("删除")
        self.deleteButton.setFixedWidth(60)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.backButton)
        Hlayout.addWidget(self.addButton)
        Hlayout.addWidget(self.deleteButton)
        widget = QWidget()
        widget.setLayout(Hlayout)
        #widget.setFixedWidth(450)
        widget.setMinimumWidth(450)
        widget.setMaximumWidth(500)
        self.Hlayout2.addWidget(widget)

        # tableView
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('db\hongwai.db')
        self.db.open()
        if not self.db.open():
            QMessageBox.critical(None, ("无法打开数据库"),
                                 ("点击取消按钮退出应用。"),
                                 QMessageBox.Cancel)
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)#不可编辑
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)#整行选中
        self.queryModel = QSqlQueryModel()
        self.queryTableModel = QSqlTableModel()
        self.queryTableModel.setTable('Users')
        self.queryTableModel.select()
        self.queryTableModel.removeColumn(0)#移除第一列
        self.searchButtonClicked()
        self.tableView.setModel(self.queryTableModel)

        self.queryTableModel.setHeaderData(0, Qt.Horizontal, "用户名")
        self.queryTableModel.setHeaderData(1, Qt.Horizontal, "密码")
        self.queryTableModel.setHeaderData(2, Qt.Horizontal, "邮箱")
        self.queryTableModel.setHeaderData(3, Qt.Horizontal, "角色")

        self.layout.addLayout(self.Hlayout1)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)
        self.addButton.clicked.connect(self.registerUser)
        self.deleteButton.clicked.connect(self.deleteItem)

    def setButtonStatus(self):
        if(self.currentPage==self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if(self.currentPage==1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if(self.currentPage<self.totalPage and self.currentPage>1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        self.totalRecord = self.queryTableModel.rowCount()
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        return

    # 点击查询
    def searchButtonClicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        #self.recordQuery(index)
        return

    # 向前翻页
    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        #self.recordQuery(index)
        return

    # 向后翻页
    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
       # self.recordQuery(index)
        return

    # 点击跳转
    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        #self.recordQuery(index)
        return

    #删除某条记录
    def deleteItem(self):
        if (QMessageBox.information(self, "提醒", "一经删除将无法恢复，是否继续?",
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No) == QMessageBox.Yes):
            currentItem = self.tableView.currentIndex().row()
            print(currentItem)
            self.queryTableModel.removeRow(currentItem)
            removeResult = self.queryTableModel.submitAll()
            print(removeResult)
            if removeResult:
                QMessageBox.information(self, "提醒", "操作成功!",
                                        QMessageBox.Yes, QMessageBox.Yes)
    #注册用户
    def registerUser(self):
        self.registerWindow = registerWindow()
        if self.registerWindow.exec_() == QtWidgets.QDialog.Accepted:
            pass

#重载注册用户对话框
class registerWindow(QtWidgets.QDialog, Ui_Form_registe):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs).__init__()
        self.setupUi(self)


#################以下是测试用####################
 #重载用户管理窗口
class UserManagerUi(QWidget, Ui_Form3):
    def __init__(self):
        super(UserManagerUi, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = UserManagerUi()
    mainMindow.show()
    sys.exit(app.exec_())
