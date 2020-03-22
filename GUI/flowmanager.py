# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flowmanager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 793)
        MainWindow.setStyleSheet("background-color: rgb(6, 22, 34);\n"
                                 "color: rgb(115, 210, 22);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.left = QtWidgets.QVBoxLayout()
        self.left.setObjectName("left")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ip_adderss = QtWidgets.QLineEdit(self.groupBox)
        self.ip_adderss.setObjectName("ip_adderss")
        self.gridLayout.addWidget(self.ip_adderss, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(self.groupBox)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Connect_server = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Connect_server.setFont(font)
        self.Connect_server.setObjectName("Connect_server")
        self.gridLayout.addWidget(self.Connect_server, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.left.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left.addItem(spacerItem)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.flow_control = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.flow_control.setFont(font)
        self.flow_control.setObjectName("flow_control")
        self.gridLayout_7.addWidget(self.flow_control, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 1, 0, 1, 1)
        self.status_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_button.setFont(font)
        self.status_button.setObjectName("status_button")
        self.gridLayout_7.addWidget(self.status_button, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 1, 2, 1, 1)
        self.flow_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.flow_button.setFont(font)
        self.flow_button.setObjectName("flow_button")
        self.gridLayout_7.addWidget(self.flow_button, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 4, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_7.addWidget(self.pushButton_8, 7, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 6, 1, 1, 1)
        self.left.addLayout(self.gridLayout_7)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.left)
        self.subwindows = QtWidgets.QVBoxLayout()
        self.subwindows.setObjectName("subwindows")
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.FieldRole, self.subwindows)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Ryu Server"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.label.setText(_translate("MainWindow", "IP Address"))
        self.Connect_server.setText(_translate("MainWindow", "Connect"))
        self.flow_control.setText(_translate("MainWindow", "Flow Control"))
        self.status_button.setText(_translate("MainWindow", "Status"))
        self.flow_button.setText(_translate("MainWindow", "Flow"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
