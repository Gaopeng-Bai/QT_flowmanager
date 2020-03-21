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

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GUI.flowmanager import Ui_MainWindow
from GUI.home import Ui_info_present
from GUI.flow_control import Ui_flow_control

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
        return 0
    elif r == 0:
        QMessageBox.about(None, "request error",
                          "Requests command not exist")
        return 0

    elif r != "no response" and r != 0:
        if r.status_code == 200:
            content = r.content.decode('utf8')
            data = json.loads(content)
            return data
        else:
            QMessageBox.about(None, "request error",
                              "Please check this requests")
            return 0


def custom_model(data):
    """
    set a table model for Qtableview. In Info_present_window.
    :param data: a dict data need to fill in table.
    :return:
    """
    model = QStandardItemModel(len(data), len(data[0]))
    model.setHorizontalHeaderLabels(data[0].keys())

    for i, row in enumerate(data):
        for j, key in enumerate(row):
            index = model.index(int(i), int(j))
            model.setData(index, row[key])
    return model


def check_to_line_edit(line):
    """
    If the line edit is empty, set 0 by default. In flow_control_window class.
    :param line: the object of line edit
    :return: the text of line edit.
    """
    if line.text() == "":
        return 0
    else:
        return line.text()


class GUI_main(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window):
        super(GUI_main, self).__init__()
        self.setupUi(main_window)
        self.ui_init()

        self.cache = None
        self.Info_present_window = Info_present_window()
        self.flow_control_window_present = flow_control_window()
        self.subwindows.addWidget(self.flow_control_window_present)
        self.subwindows.addWidget(self.Info_present_window)

        # default window
        self.home_window()

    def home_window(self):
        self.flow_control_window_present.close()
        self.Info_present_window.show()

    def flow_window(self):
        pass

    def flow_control_window(self):
        self.Info_present_window.close()
        self.flow_control_window_present.init_ui()
        self.flow_control_window_present.show()

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
            switches = get_info_by_keys(
                req_cache=self.cache, up_key="switch_ids")
            if switches:
                for switch in switches:
                    self.Info_present_window.switch_ids.addItem(switch)
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please tap in IP and Port first")


class flow_control_window(QMainWindow, Ui_flow_control):

    def __init__(self):
        super(flow_control_window, self).__init__()
        self.setupUi(self)
        self.submit.clicked.connect(self.submit_button)
        # operation
        self.add.setChecked(True)
        self.operation = 'add'
        self.add.toggled.connect(lambda: self.btn_state(self.add))
        self.modify.toggled.connect(lambda: self.btn_state(self.modify))
        self.modify_strict.toggled.connect(
            lambda: self.btn_state(self.modify_strict))
        self.delete_flow.toggled.connect(
            lambda: self.btn_state(self.delete_flow))
        self.delete_strict.toggled.connect(
            lambda: self.btn_state(self.delete_strict))
        # setValidator
        self.priority.setValidator(QIntValidator(0, 100, self))
        self.idle_timeout.setValidator(QIntValidator(0, 1000000, self))
        self.hard_timeout.setValidator(QIntValidator(0, 1000000, self))
        self.cookie.setValidator(QDoubleValidator(self))
        self.cookie_mask.setValidator(QDoubleValidator(self))
        self.output_port.setValidator(QIntValidator(-1, 100000, self))
        self.output_group.setValidator(QIntValidator(-1, 100000, self))
        self.meter_id.setValidator(QIntValidator(-1, 100000, self))

        self.goto_table.setValidator(QIntValidator(0, 100000, self))

    def init_ui(self):
        num = main_ui.Info_present_window.switch_ids.count()
        if num > 0:
            for i in range(num):
                self.switch_id_flow.addItem(
                    "SW_" + main_ui.Info_present_window.switch_ids.item(i).text())

        else:
            QMessageBox.about(None, "No switch operable",
                              "Please try to connect a server")

    def submit_button(self):
        """
        submit request with current form.
        :return:
        """
        id = self.switch_id_flow.currentText()
        if id != '':
            main_ui.cache.payload["dpid"] = id[3:]
            main_ui.cache.payload["operation"] = self.operation
            main_ui.cache.payload["table_id"] = self.table_id_flow.value()

            main_ui.cache.payload["priority"] = check_to_line_edit(
                self.priority)
            main_ui.cache.payload["idle_timeout"] = check_to_line_edit(
                self.idle_timeout)
            main_ui.cache.payload["hard_timeout"] = check_to_line_edit(
                self.hard_timeout)
            main_ui.cache.payload["cookie"] = check_to_line_edit(self.cookie)
            main_ui.cache.payload["cookie_mask"] = check_to_line_edit(
                self.cookie_mask)
            main_ui.cache.payload["out_port"] = check_to_line_edit(
                self.output_port)
            main_ui.cache.payload["out_group"] = check_to_line_edit(
                self.output_group)
            main_ui.cache.payload["meter_id"] = check_to_line_edit(
                self.meter_id)
            main_ui.cache.payload["metadata"] = check_to_line_edit(
                self.write_metadate)
            main_ui.cache.payload["metadata_mask"] = check_to_line_edit(
                self.metadate_mask)
            main_ui.cache.payload["goto"] = check_to_line_edit(self.goto_table)

            main_ui.cache.payload["matchcheckbox"] = self.match_any.isChecked()
            main_ui.cache.payload["clearactions"] = self.clear_actions.isChecked(
            )
            main_ui.cache.payload["SEND_FLOW_REM"] = self.send_flowremoved_msg.isChecked(
            )
            main_ui.cache.payload["CHECK_OVERLAP"] = self.check_overlapping.isChecked(
            )
            main_ui.cache.payload["RESET_COUNTS"] = self.reset_counts.isChecked(
            )
            main_ui.cache.payload["NO_PKT_COUNTS"] = self.do_not_count_packets.isChecked(
            )
            main_ui.cache.payload["NO_BYT_COUNTS"] = self.do_not_count_bytes.isChecked(
            )

            main_ui.cache.payload["match"] = {}
            main_ui.cache.payload["apply"] = []
            main_ui.cache.payload["write"] = {}

            response = main_ui.cache.post_flow_control()
            if response.status_code == 200:
                QMessageBox.about(None, "Done!!",
                                  "Message sent successfully")
            else:
                QMessageBox.about(None, "Warning",
                                  "Message sent failed")

        else:
            QMessageBox.about(None, "No switch operable",
                              "Please try to connect a server")

    def btn_state(self, btn):
        """
        current operation for flow
        :param btn: radio button
        :return: the operation
        """
        if btn.isChecked():
            self.operation = btn.text()

    def close(self):
        self.hide()


class Info_present_window(QMainWindow, Ui_info_present):

    def __init__(self):
        super(Info_present_window, self).__init__()
        self.setupUi(self)
        # view
        self.switch_ids.itemClicked.connect(self.show_switch_info)

    def show_switch_info(self, item):
        if main_ui.cache is not None:
            switch_desc = get_info_by_keys(
                main_ui.cache, up_key="switch_desc", switch_id=item.text())
            port_desc = get_info_by_keys(
                main_ui.cache, up_key="port_desc", switch_id=item.text())
            port_status = get_info_by_keys(
                main_ui.cache, up_key="port_status", switch_id=item.text())
            flow_summary = get_info_by_keys(
                main_ui.cache, up_key="flow_summary", switch_id=item.text())
            table_status = get_info_by_keys(
                main_ui.cache, up_key="table_status", switch_id=item.text())
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

    # Exit function, you can create an event in the code of the child window
    # that points to this function.
    def close(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # initialize application
    MainWindow = QMainWindow()  # Create main window
    main_ui = GUI_main(MainWindow)  # Create UI window
    MainWindow.show()  # present window
    # It returns 0 after the message loop ends, and then calls sys.exit (0) to
    # exit the program
    sys.exit(app.exec_())
