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

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from GUI.flowmanager import Ui_MainWindow
from server_operation.server_info import get_info


class GUI_main(Ui_MainWindow):
    def __init__(self, main_window):
        self.setupUi(main_window)
        self.ui_init()

        self.switch_data = {"switch_ids": []}

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
        # view
        self.switch_ids.itemClicked.connect(self.show_switch_info)

    def show_switch_info(self, item):
        if self.ip != '' and self.port != '':
            switch_desc = self.get_info_by_keys(up_key="switch_desc", switch_id=item.text())
            s = ""
            self.switch_desc_num.setText("Switch Desc:" + item.text())
            for key in switch_desc[item.text()]:
                s = s + str(key) + ": " + switch_desc[item.text()][key]+"\n"

            self.switch_desc.setText(s)
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please tap in IP and Port first")

    def connect_to_show(self):
        """
        Connect button slot function
        :return: None
        """
        self.ip = self.ip_adderss.text()
        self.port = self.port.text()
        if self.ip != '' and self.port != '':
            switches = self.get_info_by_keys(up_key="switch_ids")
            for switch in switches:
                self.switch_ids.addItem(switch)
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please tap in IP and Port first")

    def get_info_by_keys(self, up_key, switch_id="0"):
        """
        execute program to get information from ryu server
        :param switch_id:
        :param up_key:
        :return:
        """
        r = get_info(self.ip, self.port, up_key, switch_id)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)  # initialize application
    MainWindow = QMainWindow()  # Create main window
    ui = GUI_main(MainWindow)  # Create UI window
    MainWindow.show()  # present window
    # It returns 0 after the message loop ends, and then calls sys.exit (0) to
    # exit the program
    sys.exit(app.exec_())
