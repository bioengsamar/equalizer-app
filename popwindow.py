# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ui_mainWindow(object):
    def setupUi(self, ui_mainWindow):
        ui_mainWindow.setObjectName("ui_mainWindow")
        ui_mainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(ui_mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MplWid2 = MplWid2(self.centralwidget)
        self.MplWid2.setObjectName("MplWid2")
        self.gridLayout.addWidget(self.MplWid2, 0, 0, 1, 1)
        ui_mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui_mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        ui_mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui_mainWindow)
        self.statusbar.setObjectName("statusbar")
        ui_mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ui_mainWindow)
        QtCore.QMetaObject.connectSlotsByName(ui_mainWindow)

    def retranslateUi(self, ui_mainWindow):
        _translate = QtCore.QCoreApplication.translate
        ui_mainWindow.setWindowTitle(_translate("ui_mainWindow", "MainWindow"))

from mplwid2 import MplWid2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_mainWindow = QtWidgets.QMainWindow()
    ui = Ui_ui_mainWindow()
    ui.setupUi(ui_mainWindow)
    ui_mainWindow.show()
    sys.exit(app.exec_())

