#!/home/{username}/anaconda3 python
# encoding: utf-8
"""
@author: gaopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: gaopengbai0121@gmail.com
@software: garner
@file: Main.py
@time: 3/18/20 12:59 PM
@desc:
"""
import sys
import json

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from GUI.flowmanager import Ui_MainWindow
from GUI.home import Ui_info_present
from server_operation.server_info import req_server


def get_info_by_keys(req_cache, up_key, switch_id="0"):
    """
    execute program to get information from ryu server
    :param req_cache: the req_server object carry with ip address and port.
    :param switch_id: the id of switch to be requested.
    :param up_key: data item
    :return: the data from server response.
    """
    r = req_cache.get_info(up_key, switch_id)

    if r == "no response":
        QMessageBox.about(None, "Server no response",
                          "Please check this requests")
    elif r == 0:
        QMessageBox.about(None, "request error",
                          "Requests command not exist")

    elif r != "no response" and r != 0:
        if r.status_code == 200:
            content = r.content.decode('utf8')
            data = json.loads(content)
            return data
        else:
            QMessageBox.about(None, "request error",
                              "Please check this requests")


def custom_model(data):
    model = QStandardItemModel(len(data), len(data[0]))
    model.setHorizontalHeaderLabels(data[0].keys())

    for i, row in enumerate(data):
        for j, key in enumerate(row):
            index = model.index(int(i), int(j))
            model.setData(index, row[key])
            # item = QStandardItem(row[key])
            # model.setItem(int(i), int(j), item)
    return model


class GUI_main(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window):
        super(GUI_main, self).__init__()
        self.setupUi(main_window)
        self.ui_init()

        self.cache = None
        self.Info_present_window = Info_present_window()

        # default window
        self.home_window()

    def home_window(self):
        self.subwindows.addWidget(self.Info_present_window)
        self.Info_present_window.show()

    def flow_window(self):
        pass

    def flow_control_window(self):
        pass

    def ui_init(self):
        """
        Initialize UI function.
        :return: none
        """
        # connect group
        self.ip_adderss.setInputMask('000.000.000.000')
        self.ip_adderss.setText("127.0.0.1")
        self.port.setInputMask('00000')
        self.port.setText('8080')
        self.Connect_server.clicked.connect(self.connect_to_show)
        # status button connect to home window
        self.status_button.clicked.connect(self.home_window)
        # flow button connect to flow viewer
        self.flow_button.clicked.connect(self.flow_window)
        # flow control button
        self.flow_control.clicked.connect(self.flow_control_window)

    def connect_to_show(self):
        """
        Connect button slot function
        :return: None
        """
        ip = self.ip_adderss.text()
        port = self.port.text()
        if ip != '' and port != '':
            self.cache = req_server(ip=ip, port=port)
            switches = get_info_by_keys(req_cache=self.cache, up_key="switch_ids")
            for switch in switches:
                self.Info_present_window.switch_ids.addItem(switch)
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please tap in IP and Port first")


class Info_present_window(QMainWindow, Ui_info_present):

    def __init__(self):
        super(Info_present_window, self).__init__()
        self.setupUi(self)
        # view
        self.switch_ids.itemClicked.connect(self.show_switch_info)

    def show_switch_info(self, item):
        if ui.cache is not None:
            switch_desc = get_info_by_keys(ui.cache, up_key="switch_desc", switch_id=item.text())
            port_desc = get_info_by_keys(ui.cache, up_key="port_desc", switch_id=item.text())
            port_status = get_info_by_keys(ui.cache, up_key="port_status", switch_id=item.text())
            flow_summary = get_info_by_keys(ui.cache, up_key="flow_summary", switch_id=item.text())
            table_status = get_info_by_keys(ui.cache,up_key="table_status", switch_id=item.text())
            # fill the switch desc
            s = ""
            self.switch_desc_num.setText("Switch Desc:" + item.text())
            for key in switch_desc[item.text()]:
                s = s + str(key) + ": " + switch_desc[item.text()][key] + "\n"
            self.switch_desc.setText(s)
            # fill port desc
            self.port_desc.setModel(custom_model(port_desc[item.text()]))
            # fill port status
            self.port_status.setModel(custom_model(port_status[item.text()]))
            # fill flow summary
            self.flow_summary.setModel(custom_model(flow_summary[item.text()]))
            # fill table status
            self.table_status.setModel(custom_model(table_status[item.text()]))
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please connect available server first")

    # Exit function, you can create an event in the code of the child window that points to this function.
    def close(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # initialize application
    MainWindow = QMainWindow()  # Create main window
    ui = GUI_main(MainWindow)  # Create UI window
    MainWindow.show()  # present window
    # It returns 0 after the message loop ends, and then calls sys.exit (0) to
    # exit the program
    sys.exit(app.exec_())
