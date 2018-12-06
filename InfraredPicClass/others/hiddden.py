# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore,QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        fileMenu = self.menuBar().addMenu('File')
        self.newMenu = QtWidgets.QMenu(fileMenu)
        self.newMenu.setTitle('New')
        self.newMenu.addAction('New Word')
        self.newMenu.addAction('New Excel')
        self.newAction = fileMenu.addMenu(self.newMenu)
        self.saveAction = fileMenu.addAction('Save')

        editMenu = self.menuBar().addMenu('Edit')
        hideAction = editMenu.addAction('Hide')
        self.connect(hideAction, QtCore.SIGNAL('triggered()'), self.hideMenu)

    def hideMenu(self):
        self.newAction.setVisible(False)
        self.saveAction.setVisible(False)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())