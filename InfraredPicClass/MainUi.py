from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QFileDialog, QTreeView, QTreeWidget,
                             QTreeWidgetItem,QToolBox,QWidget)
from PIL import Image
from EditImage import Ui_Form
from ImageView import Ui_Form0
import ImageView
from ImageLibUi import Ui_Form2
from UserManager import Ui_Form3
import qdarkstyle
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        # 文件树形目录浏览器
        self.tree = QTreeView()
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath('')
        self.nameFile = ["*.png", "*.jpg", "*.jpeg"]
        self.model.setNameFilterDisables(False)
        self.model.setNameFilters(self.nameFile)
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setWindowTitle("Dir View")
        self.tree.setSortingEnabled(True)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)
        self.tree.doubleClicked.connect(self.openFileFromTreeList)
        # 图库管理器
        self.tree_2 = QTreeWidget()
        self.tree_2.setColumnCount(1)
        # 设置表头信息：隐藏表头
        self.tree_2.setHeaderHidden(1)
        # 设置root和root2为self.tree的子树，所以root和root2就是跟节点
        root = QTreeWidgetItem(self.tree_2)
        root2 = QTreeWidgetItem(self.tree_2)
        # 设置根节点的名称
        root.setText(0, '第一节点')
        root2.setText(0, '第二节点')
        # 为root节点设置子结点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'name1')
        child2 = QTreeWidgetItem(root)
        # 设置child2节点的图片
        child2.setText(0, 'child2')
        child2.setText(1, 'name2')

        # 实例化QToolBox
        self.toolBox = QToolBox()
        # 设置左侧导航栏 toolBox 在左右拉拽时的最小宽度
        self.toolBox.setMinimumWidth(100)
        # 给QToolBox添加两个子项目
        self.toolBox.addItem(self.tree, "文件资源")
        self.toolBox.addItem(self.tree_2, "图库")

        # 给QSplitter添加第一个窗体（QToolBox）
        self.splitter.addWidget(self.toolBox)

        #菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(10, 10, 820, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.menu1_file = QtWidgets.QMenu(self.menubar)
        self.menu1_file.setObjectName("menu1_file")
        self.menu2_edit = QtWidgets.QMenu(self.menubar)
        self.menu2_edit.setObjectName("menu2_edit")
        self.menu3_imageLib = QtWidgets.QMenu(self.menubar)
        self.menu3_imageLib.setObjectName("menu3_imageLib")
        self.menu4_image = QtWidgets.QMenu(self.menubar)
        self.menu4_image.setObjectName("menu4_image")
        self.menu6_user = QtWidgets.QMenu(self.menubar)
        self.menu6_user.setObjectName("menu6_user")
        self.menu5_help = QtWidgets.QMenu(self.menubar)
        self.menu5_help.setObjectName("menu5_help")
        MainWindow.setMenuBar(self.menubar)

        #menu Action
        #################action1######################
        self.action_1_1 = QtWidgets.QAction(MainWindow)
        self.action_1_1.setObjectName("action_1_1")#打开
        self.action_1_1.triggered.connect(self.openfile)
        self.action_1_2 = QtWidgets.QAction(MainWindow)
        self.action_1_2.setObjectName("action_1_2")#保存
        self.action_1_3 = QtWidgets.QAction(MainWindow)
        self.action_1_3.setObjectName("action_1_3")#退出
        #################action2######################
        self.action_2_1 = QtWidgets.QAction(MainWindow)
        self.action_2_1.setObjectName("action_2_1")#图片编辑
        self.action_2_1.triggered.connect(self.openChildWindow)
        #################action3######################
        self.action_3_1 = QtWidgets.QAction(MainWindow)
        self.action_3_1.setObjectName("action_3_1")#图库管理器
        self.action_3_1.triggered.connect(self.imageLibUi)
        #################action4######################
        self.action_4_1 = QtWidgets.QAction(MainWindow)
        self.action_4_1.setObjectName("action_4_1")  # 添加图片
        self.action_4_2 = QtWidgets.QAction(MainWindow)
        self.action_4_2.setObjectName("action_4_2")  # 删除图片
        self.action_4_3 = QtWidgets.QAction(MainWindow)
        self.action_4_3.setObjectName("action_4_3")  # 重命名
        #################action5######################
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")#帮助
        #################action6######################
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")#用户管理
        self.action_6.triggered.connect(self.userManager)

        #给menu添加Action
        self.menu1_file.addAction(self.action_1_1)#打开
        self.menu1_file.addAction(self.action_1_2)#保存
        self.menu1_file.addAction(self.action_1_3)#退出
        self.menu2_edit.addAction(self.action_2_1)#图片编辑
        self.menu3_imageLib.addAction(self.action_3_1)#图库管理器
        self.menu4_image.addAction(self.action_4_1)#添加图片
        self.menu4_image.addAction(self.action_4_2)#删除图片
        self.menu4_image.addAction(self.action_4_3)#重命名
        self.menu6_user.addAction(self.action_6)#用户管理
        self.menu5_help.addAction(self.action_5)#帮助
        self.menubar.addAction(self.menu1_file.menuAction())
        self.menubar.addAction(self.menu2_edit.menuAction())
        self.menubar.addAction(self.menu3_imageLib.menuAction())
        self.menubar.addAction(self.menu4_image.menuAction())
        self.menubar.addAction(self.menu5_help.menuAction())
        self.menubar.addAction(self.menu6_user.menuAction())

        #Icon
        icon = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/openfile.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Icon/edit.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_1_1.setIcon(icon)
        self.action_2_1.setIcon(icon2)

        #工具栏
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhSensitiveData)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.addAction(self.action_1_1)
        self.toolBar.addAction(self.action_2_1)

        #状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #初始化默认窗体
        #初始化默认窗体（图片显示窗体）
        self.imageView = ImageView()
        # 在主窗口里添加子窗口
        self.splitter.addWidget(self.imageView)

        #是普通用户还是管理员
        self

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 创建默认存放文件的文件夹：
        cur_dir = "C:"
        folder_name = 'InfraredImage'
        if os.path.isdir("C:/InfraredImage"):
            print("Already exist!")
        else:
            os.mkdir(os.path.join(cur_dir, folder_name))
            os.mkdir("C:/InfraredImage/TmpImg")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "红外图像质量客观评价系统V1.0"))

        #导航栏名字
        self.menu1_file.setTitle(_translate("MainWindow", "文件"))
        self.menu3_imageLib.setTitle(_translate("MainWindow", "图库管理"))
        self.menu4_image.setTitle(_translate("MainWindow", "图片管理"))
        self.menu2_edit.setTitle(_translate("MainWindow", "编辑"))
        self.menu6_user.setTitle(_translate("MainWindow", "用户管理"))
        self.menu5_help.setTitle(_translate("MainWindow", "帮助"))

        #action名字
        self.action_1_1.setText(_translate("MainWindow", "打开"))
        self.action_1_1.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_1_2.setText(_translate("MainWindow", "保存"))
        self.action_1_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_1_3.setText(_translate("MainWindow", "退出"))
        self.action_1_3.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_2_1.setText(_translate("MainWindow", "编辑图片"))
        self.action_3_1.setText(_translate("MainWindow", "图库管理器"))
        self.action_4_1.setText(_translate("MainWindow", "添加图片"))
        self.action_4_2.setText(_translate("MainWindow", "删除图片"))
        self.action_4_3.setText(_translate("MainWindow", "重命名"))
        self.action_5.setText(_translate("MainWindow", "Help ?"))
        self.action_6.setText(_translate("MainWindow", "用户管理器"))

        self.statusbar.showMessage("Ready")

    ##########################功能函数区###############################

    def openfile(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        fileName1, filetype = QFileDialog.getOpenFileName(None,
                                                          "选取文件",
                                                          "C:/",
                                                          "All Files (*);;Image (*.png *.jpg *.jpeg)")
        #显示图片，并初始化图片基本信息
        self.openImage(fileName1)

    # 从文件资源目录树打开图片
    def openFileFromTreeList(self, Qmodelidx):
        filePath = self.model.filePath(Qmodelidx)
        self.openImage(filePath)

        # 打开图片,并初始化图片基本信息
    def openImage(self, filePath):
        self.action_2_1.setEnabled(True)
        self.splitter.widget(1).setParent(None)
        self.splitter.insertWidget(1, self.imageView)
        img = QtGui.QPixmap(filePath).scaled(self.imageView.graphicsView.width(), self.imageView.graphicsView.height())
        self.imageView.graphicsView.setPixmap(img)
        self.newPic = Image.open(filePath)
        self.statusbar.showMessage("打开图片")
        self.imageView.listWidget.item(1).setText("大小： " + str(self.newPic.size))
        self.imageView.listWidget.item(2).setText("色彩通道： " + self.newPic.mode)
        self.imageView.listWidget.item(3).setText("格式： " + self.newPic.format)
        self.imageView.listWidget.item(4).setText("像素： " + str(self.newPic.getextrema()))
        self.imageView.listWidget.item(5).setText("文件： " + str(filePath))
        # # 要把新打开的图片，和所有修改过的图片，都存进tempPic.jpg里面，作为一个中间变量。
        self.newPic.save("C:/InfraredImage/TmpImg/tempPic.png")
        self.newPic = "C:/InfraredImage/TmpImg/tempPic.png"

    # 打开图片处理子窗口函
    def openChildWindow(self):
        childUi = childWindow()
        if childUi.exec_() == QtWidgets.QDialog.Accepted:
            pass

    #打开图库管理窗口
    def imageLibUi(self):
        self.imageLibUi = ImageLibUi()
        # 把QSplitter的指定位置的窗体从QSplitter中剥离
        self.splitter.widget(1).setParent(None)
        # 在QSplitter的指定位置载入新窗体
        self.splitter.insertWidget(1, self.imageLibUi)
        # 打开图库管理窗口时将图片编辑器设为不可用
        self.action_2_1.setEnabled(False)

     #用户管理
    def userManager(self):
        self.userWindow = UserManagerUi()
        # 把QSplitter的指定位置的窗体从QSplitter中剥离
        self.splitter.widget(1).setParent(None)
        # 在QSplitter的指定位置载入新窗体
        self.splitter.insertWidget(1, self.userWindow)
        # 打开图库管理窗口时将图片编辑器设为不可用
        self.action_2_1.setEnabled(False)

# 重载图片处理窗口
class childWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs).__init__()
        self.setupUi(self)

#重载用户管理窗口
class UserManagerUi(QWidget, Ui_Form3):
    def __init__(self):
        super(UserManagerUi, self).__init__()
        self.setupUi(self)

  #重载图库管理窗口
class ImageLibUi(QWidget, Ui_Form2):
    def __init__(self):
        super(ImageLibUi, self).__init__()
        self.setupUi(self)

#重载图片显示窗体
class ImageView(QWidget, Ui_Form0):
    def __init__(self):
        super(ImageView, self).__init__()
        #子窗口初始化是实现子窗口布局
        self.setupUi(self)