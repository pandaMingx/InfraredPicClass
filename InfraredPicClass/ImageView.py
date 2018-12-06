
from PyQt5 import QtCore, QtGui, QtWidgets
#图片处理模块PIL
from PIL import Image

class Ui_Form0(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 610)
        Form.setAutoFillBackground(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # 放图片的View
        self.graphicsView = QtWidgets.QLabel()
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("border: 2px solid rgb(128, 138, 135)")
        self.graphicsView.setMinimumHeight(420)
        self.graphicsView.setMaximumHeight(540)
        self.graphicsView.setMaximumWidth(600)
        self.graphicsView.setMinimumWidth(420)
        #显示图片基本信息的listWidgets
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "图片属性:"))
