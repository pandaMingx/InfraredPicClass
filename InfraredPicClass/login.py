# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loging.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
import qdarkstyle
import hashlib
import sys
#from MainService import MainWindow


class Ui_Form_login(object):
    def setupUi(self, Form):

        self.is_admin_signal = pyqtSignal()
        self.is_commonUser_signal = pyqtSignal()

        Form.setObjectName("Form")
        Form.resize(395, 242)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)#密码不显示明文
        self.LoginButton = QtWidgets.QPushButton(Form)
        self.LoginButton.setGeometry(QtCore.QRect(60, 190, 75, 23))
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.signInCheck)
        self.RegisterButton = QtWidgets.QPushButton(Form)
        self.RegisterButton.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.RegisterButton.setObjectName("RegisterButton")
        self.RegisterButton.clicked.connect(self.gotoRegiste)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 50, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 89, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 131, 16))
        self.label_3.setObjectName("label_3")
        self.actionLogin = QtWidgets.QAction(Form)
        self.actionLogin.setObjectName("actionLogin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LoginButton.setText(_translate("Form", "登录"))
        self.RegisterButton.setText(_translate("Form", "注册"))
        self.label.setText(_translate("Form", "用户名"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "红外图像质量检测系统"))
        self.actionLogin.setText(_translate("Form", "Login"))

        #用户登录验证
    def signInCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if (username == "" or password == ""):
            QMessageBox.warning(None, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes)
            return
        # 打开数据库连接
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('db\hongwai.db')
        db.open()
        if not db.open():
            QMessageBox.critical(None, ("无法打开数据库"),
                                 ("点击取消按钮退出应用。"),
                                 QMessageBox.Cancel)
        query = QSqlQuery()
        sql = "SELECT * FROM Users WHERE username='%s'" % username
        query.exec_(sql)
        db.close()
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        if not query.next():
            QMessageBox.information(None, "提示", "该账号不存在!",
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            if username == query.value(1) and password == query.value(2):
                if query.value(3) == "0":
                    self.is_admin_signal.emit()
                if query.value(3) == "1":
                    self.is_commonUser_signal.emit()
                #Ui_Main.show()
                loginwindow().accept()
                #widget.close()
            else:
                QMessageBox.information(None, "提示", "密码错误!",
                                        QMessageBox.Yes, QMessageBox.Yes)
        return

    #转到注册界面
    def gotoRegiste(self):
        QMessageBox.information(None, "提示", "注册账号请联系管理员",
                                QMessageBox.Yes, QMessageBox.Yes)


class loginwindow(QtWidgets.QDialog, Ui_Form_login):
    def __init__(self, *args, **kwargs):
        super(loginwindow, self).__init__(*args, **kwargs)
        Ui_Form_login.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/main.png"))
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    loginWindow = Ui_Form_login()
    #Ui_Main = MainWindow()#此处需要先初始化主窗口
    widget = QtWidgets.QMainWindow()
    loginWindow.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
