# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon
from login import loginwindow
import qdarkstyle
import hashlib
import sys

class Ui_Form_registe(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.cb = QtWidgets.QComboBox(Form)
        self.cb.addItem("0")
        self.cb.addItem("1")
        self.cb.setGeometry(QtCore.QRect(140, 210, 90, 20))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registCheck)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ifcancel)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 56, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QtCore.QRect(80, 210, 51, 21))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "用户名"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "确认密码"))
        self.label_4.setText(_translate("Form", "邮箱"))
        self.label_5.setText(_translate("Form", "红外图像质量检测系统"))
        self.label_6.setText(_translate("Form", "角色"))

    #用户注册业务逻辑
    def registCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmPassword = self.lineEdit_3.text()
        mail = self.lineEdit_4.text()
        role = self.cb.currentText()
        if (username == "" or mail == "" or password == ""
                or confirmPassword == "" or role == ""):
            QMessageBox.warning(None, "警告", "表单不可为空，请重新输入",
                                QMessageBox.Yes, QMessageBox.Yes)
            return
        else:  # 需要处理逻辑，1.账号已存在;2.密码不匹配;3.插入user表
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('db\hongwai.db')
            db.open()
            if not db.open():
                QMessageBox.critical(None, ("无法打开数据库"),
                                     ("点击取消按钮退出应用。"),
                                     QMessageBox.Cancel)
            query = QSqlQuery()
            if (confirmPassword != password):
                QMessageBox.warning(None, "警告", "两次输入密码不一致，请重新输入",
                                    QMessageBox.Yes, QMessageBox.Yes)
                return
            elif (confirmPassword == password):
                # md5编码
                hl = hashlib.md5()
                hl.update(password.encode(encoding='utf-8'))
                md5password = hl.hexdigest()
                sql = "SELECT * FROM Users WHERE username='%s'" % (username)
                query.exec_(sql)
                if (query.next()):
                    QMessageBox.warning(None, "警告", "该账号已存在,请重新输入",
                                        QMessageBox.Yes, QMessageBox.Yes)
                    return
                else:
                    sql = "INSERT INTO Users VALUES (null,'%s','%s','%s','%s')" % (
                        username, password, mail,role)
                    db.exec_(sql)
                    db.commit()
                    QMessageBox.information(None, "提醒", "您已成功注册账号!",
                                            QMessageBox.Yes, QMessageBox.Yes)
                    loginWindow.show()
                    widget.close()
                db.close()
                return

        #取消时返回登录界面
    def ifcancel(self):
        widget.close()

#重载
class registwindow(QtWidgets.QMainWindow, Ui_Form_registe):
    def __init__(self):
        super(registwindow, self).__init__()
        Ui_Form_registe.__init__(self)
        self.setupUi(self)

#程序入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/main.png"))
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    registWindow = registwindow()
    loginWindow = loginwindow()
    widget = QtWidgets.QMainWindow()
    registWindow.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

