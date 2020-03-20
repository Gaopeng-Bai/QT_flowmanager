# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info_present(object):
    def setupUi(self, info_present):
        info_present.setObjectName("info_present")
        info_present.resize(785, 673)
        info_present.setStyleSheet("background-color: rgb(85, 87, 83);\n"
                                   "color: rgb(115, 210, 22);")
        self.layoutWidget = QtWidgets.QWidget(info_present)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 767, 655))
        self.layoutWidget.setObjectName("layoutWidget")
        self.showframe = QtWidgets.QGridLayout(self.layoutWidget)
        self.showframe.setContentsMargins(0, 0, 0, 0)
        self.showframe.setObjectName("showframe")
        self.flow_summary = QtWidgets.QTableView(self.layoutWidget)
        self.flow_summary.setObjectName("flow_summary")
        self.showframe.addWidget(self.flow_summary, 5, 1, 1, 1)
        self.switch_desc_num_4 = QtWidgets.QLabel(self.layoutWidget)
        self.switch_desc_num_4.setObjectName("switch_desc_num_4")
        self.showframe.addWidget(self.switch_desc_num_4, 2, 1, 1, 1)
        self.switch_desc_num = QtWidgets.QLabel(self.layoutWidget)
        self.switch_desc_num.setObjectName("switch_desc_num")
        self.showframe.addWidget(self.switch_desc_num, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem, 1, 4, 1, 1)
        self.switch_desc_num_2 = QtWidgets.QLabel(self.layoutWidget)
        self.switch_desc_num_2.setObjectName("switch_desc_num_2")
        self.showframe.addWidget(self.switch_desc_num_2, 2, 3, 1, 1)
        self.switch_desc = QtWidgets.QTextBrowser(self.layoutWidget)
        self.switch_desc.setObjectName("switch_desc")
        self.showframe.addWidget(self.switch_desc, 1, 3, 1, 1)
        self.switch_desc_num_3 = QtWidgets.QLabel(self.layoutWidget)
        self.switch_desc_num_3.setObjectName("switch_desc_num_3")
        self.showframe.addWidget(self.switch_desc_num_3, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem1, 1, 0, 1, 1)
        self.table_status = QtWidgets.QTableView(self.layoutWidget)
        self.table_status.setObjectName("table_status")
        self.showframe.addWidget(self.table_status, 5, 3, 1, 1)
        self.port_desc = QtWidgets.QTableView(self.layoutWidget)
        self.port_desc.setObjectName("port_desc")
        self.showframe.addWidget(self.port_desc, 3, 1, 1, 1)
        self.port_status = QtWidgets.QTableView(self.layoutWidget)
        self.port_status.setObjectName("port_status")
        self.showframe.addWidget(self.port_status, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.showframe.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.showframe.addWidget(self.label_3, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.showframe.addItem(spacerItem2, 1, 2, 1, 1)
        self.switch_ids = QtWidgets.QListWidget(self.layoutWidget)
        self.switch_ids.setObjectName("switch_ids")
        self.showframe.addWidget(self.switch_ids, 1, 1, 1, 1)

        self.retranslateUi(info_present)
        QtCore.QMetaObject.connectSlotsByName(info_present)

    def retranslateUi(self, info_present):
        _translate = QtCore.QCoreApplication.translate
        info_present.setWindowTitle(_translate("info_present", "Form"))
        self.switch_desc_num_4.setText(_translate("info_present", "Port Desc"))
        self.switch_desc_num.setText(_translate("info_present", "Switch IDs"))
        self.switch_desc_num_2.setText(
            _translate("info_present", "Port status"))
        self.switch_desc_num_3.setText(
            _translate("info_present", "Switch Desc"))
        self.label_4.setText(_translate("info_present", "Table status"))
        self.label_3.setText(_translate("info_present", "Flow summary"))
