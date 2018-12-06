# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon
import qdarkstyle
import hashlib
import sys

class Ui_Form_addImage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 150, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 150, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addImageLib)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.clicked.connect()
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 140, 60, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.selectFile)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 70, 50, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 70, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 131, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "添加"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton_3.setText(_translate("Form", "浏览"))
        self.label.setText(_translate("Form", "图库名"))
        self.label_2.setText(_translate("Form", "选择文件夹"))
        self.label_5.setText(_translate("Form", "添加图库"))

    #向数据库添加一个图库
    def addImageLib(self):
        imagelibname = self.lineEdit.text()
        directory = self.lineEdit_2.text()
        if (imagelibname == "" or directory == ""):
            QMessageBox.warning(None, "警告", "表单不可为空，请重新输入",
                                QMessageBox.Yes, QMessageBox.Yes)
            return
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('db\hongwai.db')
            db.open()
            if not db.open():
                QMessageBox.critical(None, ("无法打开数据库"),
                                     ("点击取消按钮退出应用。"),
                                     QMessageBox.Cancel)
            #query = QSqlQuery()
            sql = "INSERT INTO ImageLibrary VALUES (null,'%s','%s')" % (imagelibname, directory)
            db.exec_(sql)
            db.commit()
            QMessageBox.information(None, "提醒", "操作成功",
                                        QMessageBox.Yes, QMessageBox.Yes)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            db.close()
            return

    def selectFile(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        directory = QFileDialog.getExistingDirectory(None,
                                                              "选取文件",
                                                              "C:/InfraredImage/ImageLib")
        # 浏览文件夹，并将路径赋值给文本框
        self.lineEdit_2.setText(directory)

#########以下是测试用##########
#重载
class registwindow(QtWidgets.QMainWindow, Ui_Form_addImage):
    def __init__(self):
        super(registwindow, self).__init__()
        Ui_Form_addImage.__init__(self)
        self.setupUi(self)
#程序入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/main.png"))
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    registWindow = registwindow()
    widget = QtWidgets.QMainWindow()
    registWindow.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

