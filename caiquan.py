# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caiquan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.biaoti = QtWidgets.QLabel(self.centralwidget)
        self.biaoti.setGeometry(QtCore.QRect(10, 0, 201, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.biaoti.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.biaoti.setFont(font)
        self.biaoti.setObjectName("biaoti")
        self.shuangren = QtWidgets.QPushButton(self.centralwidget)
        self.shuangren.setGeometry(QtCore.QRect(50, 110, 221, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.shuangren.setFont(font)
        self.shuangren.setObjectName("shuangren")
        self.sanren = QtWidgets.QPushButton(self.centralwidget)
        self.sanren.setGeometry(QtCore.QRect(50, 280, 221, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.sanren.setFont(font)
        self.sanren.setObjectName("sanren")
        self.siren = QtWidgets.QPushButton(self.centralwidget)
        self.siren.setGeometry(QtCore.QRect(50, 450, 221, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.siren.setFont(font)
        self.siren.setObjectName("siren")
        self.jieshu = QtWidgets.QPushButton(self.centralwidget)
        self.jieshu.setGeometry(QtCore.QRect(980, 690, 111, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.jieshu.setFont(font)
        self.jieshu.setObjectName("jieshu")
        self.tupian = QtWidgets.QLabel(self.centralwidget)
        self.tupian.setGeometry(QtCore.QRect(560, 580, 200, 181))
        self.tupian.setText("")
        self.tupian.setObjectName("tupian")
        self.jilu = QtWidgets.QPushButton(self.centralwidget)
        self.jilu.setGeometry(QtCore.QRect(810, 610, 111, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.jilu.setFont(font)
        self.jilu.setObjectName("jilu")
        self.jingyin = QtWidgets.QCheckBox(self.centralwidget)
        self.jingyin.setGeometry(QtCore.QRect(990, 600, 201, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.jingyin.setFont(font)
        self.jingyin.setObjectName("jingyin")
        self.fanhui = QtWidgets.QPushButton(self.centralwidget)
        self.fanhui.setGeometry(QtCore.QRect(810, 690, 111, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.fanhui.setFont(font)
        self.fanhui.setObjectName("fanhui")
        self.jieguo = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo.setGeometry(QtCore.QRect(30, 570, 491, 191))
        self.jieguo.setObjectName("jieguo")
        self.xianshi = QtWidgets.QLabel(self.centralwidget)
        self.xianshi.setGeometry(QtCore.QRect(450, 108, 701, 401))
        self.xianshi.setText("")
        self.xianshi.setObjectName("xianshi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.biaoti.setText(_translate("MainWindow", "    猜拳小子！"))
        self.shuangren.setText(_translate("MainWindow", "双人模式"))
        self.sanren.setText(_translate("MainWindow", "三人模式"))
        self.siren.setText(_translate("MainWindow", "四人模式"))
        self.jieshu.setText(_translate("MainWindow", "结束"))
        self.jilu.setText(_translate("MainWindow", "战绩"))
        self.jingyin.setText(_translate("MainWindow", "静音"))
        self.fanhui.setText(_translate("MainWindow", "返回"))
