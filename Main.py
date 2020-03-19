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
        self.ip_adderss.setInputMask('000.000.000.000')
        self.ip_adderss.setText("127.0.0.1")
        self.port.setInputMask('00000')
        self.port.setText('8080')
        self.Connect_server.clicked.connect(self.connect_to_show)

    def connect_to_show(self):
        """
        Connect button slot function
        :return: None
        """
        ip = self.ip_adderss.text()
        port = self.port.text()
        if ip != '' and port != '':
            self.show_server_info(ip, port)
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please tap in IP and Port first")

    def show_server_info(self, ip, port, req_key="switch_ids"):
        """
        execute program to get information from ryu server
        :param req_key:
        :param ip:
        :param port:
        :return:
        """
        r = get_info(ip, port, req_key)

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
                for switch in data:
                    print(switch)
                    self.switch_data[req_key].
                    # s = ""
                    # self.switch_desc_num.setText("Switch Desc:" + switch)
                    # for key in data[switch]:
                    #     s = s + str(key) + ": " + data[switch][key]+"\n"
                    #
                    # self.switch_desc.setText(s)

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
