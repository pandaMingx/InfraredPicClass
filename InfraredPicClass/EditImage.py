from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PIL import Image,ImageFilter,ImageFont,ImageDraw,ImageEnhance
import PIL

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 411)
        self.graphicsView = QtWidgets.QLabel(Form)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 371, 331))
        self.graphicsView.setObjectName("graphicsView")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(0, 380, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.bigger)#放大
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(80, 380, 71, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.smaller)#缩小
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(160, 380, 71, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.rotate90Pic)#旋转90度
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(240, 380, 71, 31))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.clicked.connect(self.rotatePic)  # 翻转
        self.toolButton_5 = QtWidgets.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(320, 380, 71, 31))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.mirrorPic) #镜面
        self.toolButton_6 = QtWidgets.QToolButton(Form)
        self.toolButton_6.setGeometry(QtCore.QRect(400, 380, 71, 31))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        self.toolButton_7.setGeometry(QtCore.QRect(480, 380, 71, 31))
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(420, 50, 211, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.valueChanged.connect(self.fuzzy)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 20, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 51, 21))
        self.label_2.setObjectName("label_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(420, 130, 211, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.valueChanged.connect(self.sharpen)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 180, 51, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(420, 210, 211, 16))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        # 定义了一些图片，filename存放的是打开图片的文件名，newPic存放P图后的文件，
        self.filename = "C:/InfraredImage/TmpImg/temPic.png"
        self.newPic = "C:/InfraredImage/TmpImg/tempPic.png"
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片处理"))
        self.toolButton.setText(_translate("Form", "放大"))
        self.toolButton_2.setText(_translate("Form", "缩小"))
        self.toolButton_3.setText(_translate("Form", "旋转"))
        self.toolButton_4.setText(_translate("Form", "翻转"))
        self.toolButton_5.setText(_translate("Form", "镜面"))
        self.toolButton_6.setText(_translate("Form", "剪切"))
        self.toolButton_7.setText(_translate("Form", "保存"))
        self.label.setText(_translate("Form", "模糊化"))
        self.label_2.setText(_translate("Form", "锐化"))
        self.label_3.setText(_translate("Form", "亮度"))
        #打开图片处理器后从缓存中把图片读取出来
        img = QtGui.QPixmap(self.newPic).scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.setPixmap(img)

##########################################功能函数############################

        #图片放大
    def bigger(self):
        img = cv2.imread(self.newPic)
        res = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(self.filename, res)
        # 在画面上展示一下效果：
        self.pic = QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)
        self.newPic = self.filename

        #缩小
    def smaller(self):
        img = cv2.imread(self.newPic)
        res = cv2.resize(img, None, fx=2/3, fy=2/3, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(self.filename, res)
        # 在画面上展示一下效果：
        self.pic = QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)
        self.newPic = self.filename

        #翻转
    def rotatePic(self):
        getPic=Image.open(self.newPic)
        self.newPic=getPic.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.newPic.save(self.filename)
        self.newPic=self.filename
        self.pic=QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)

       #旋转 90度
    def rotate90Pic(self):
        getPic=Image.open(self.newPic)
        self.newPic=getPic.transpose(PIL.Image.ROTATE_90)
        self.newPic.save(self.filename)
        self.newPic=self.filename
        self.pic=QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)

        #镜面
    def mirrorPic(self):
        getPic=Image.open(self.newPic)
        self.newPic=getPic.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        self.newPic.save(self.filename)
        self.newPic=self.filename
        self.pic=QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)

        #模糊化
    def fuzzy(self):
        getPic = Image.open(self.newPic)
        fuzzyValue = self.horizontalSlider.value()
        self.newPic = getPic.filter(ImageFilter.GaussianBlur(radius=fuzzyValue))#高斯模糊
        self.newPic.save(self.filename)
        self.newPic = self.filename
        self.pic = QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)

        #锐化
    def sharpen(self):
        gerPic = Image.open(self.newPic)
        sharpenValue = self.horizontalSlider_2.value()
        self.newPic = gerPic.filter(ImageFilter.UnsharpMask(radius=sharpenValue,percent=300,threshold=3))
        self.newPic.save(self.filename)
        self.newPic = self.filename
        self.pic = QtGui.QPixmap(self.filename)
        self.graphicsView.setPixmap(self.pic)