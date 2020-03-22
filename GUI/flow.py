# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_flow(object):
    def setupUi(self, flow):
        flow.setObjectName("flow")
        flow.resize(879, 682)
        flow.setStyleSheet("background-color: rgb(85, 87, 83);\n"
                           "color: rgb(115, 210, 22);")
        self.flow_switch_ids = QtWidgets.QComboBox(flow)
        self.flow_switch_ids.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.flow_switch_ids.setObjectName("flow_switch_ids")
        self.delete_flow = QtWidgets.QPushButton(flow)
        self.delete_flow.setGeometry(QtCore.QRect(670, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.delete_flow.setFont(font)
        self.delete_flow.setObjectName("delete_flow")
        self.flow_table_view = QtWidgets.QTableWidget(flow)
        self.flow_table_view.setGeometry(QtCore.QRect(10, 70, 821, 581))
        self.flow_table_view.setObjectName("flow_table_view")
        self.flow_table_view.setColumnCount(0)
        self.flow_table_view.setRowCount(0)

        self.retranslateUi(flow)
        QtCore.QMetaObject.connectSlotsByName(flow)

    def retranslateUi(self, flow):
        _translate = QtCore.QCoreApplication.translate
        flow.setWindowTitle(_translate("flow", "Form"))
        self.delete_flow.setText(_translate("flow", "Delete"))
