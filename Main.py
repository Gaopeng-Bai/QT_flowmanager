#!/home/{username}/anaconda3 python
# encoding: utf-8
"""
@author: li weishi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 2018787853@qq.com
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
from GUI.flow import Ui_flow

from server_operation.server_info import req_server


def read_json_(path):
    """
    read json file for match filed, action type.
    :param path: json file path
    :return: filed list and value list.
    """
    with open(path, 'r') as f:
        data = json.load(f)
        a = []
        b = []
        for key in data:
            a.append(key)
            b.append(data[key][1])

        return a, b


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
        return False
    elif r == 0:
        QMessageBox.about(None, "request error",
                          "Requests command not exist")
        return False

    elif r != "no response" and r != 0:
        if r.status_code == 200:
            content = r.content.decode('utf8')
            data = json.loads(content)
            return data
        else:
            QMessageBox.about(None, "request error" + str(r.status_code),
                              "Please check this requests")
            return False


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
            model.setData(index, str(row[key]))
    return model


def check_to_line_edit(line):
    """
    If the line edit is empty, set 0 by default. In flow_control_window class.
    :param line: the object of line edit
    :return: the text of line edit.
    """
    if line.text() == "":
        return int(0)
    else:
        return int(line.text())


class GUI_main(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window):
        super(GUI_main, self).__init__()
        self.setupUi(main_window)
        self.ui_init()
        self.sub = QStackedLayout(self.subwindows)

        self.cache = None
        self.Info_present_window = Info_present_window()
        self.flows_viewer = flow_present_window()
        self.flow_control_window_present = flow_control_window()
        self.sub.addWidget(self.Info_present_window)
        self.sub.addWidget(self.flows_viewer)
        self.sub.addWidget(self.flow_control_window_present)

    def show_panel(self):
        dic = {
            "status_button": 0,
            "flow_button": 1,
            "flow_control": 2,
        }
        index = dic[self.sender().objectName()]
        self.sub.setCurrentIndex(index)
        if index == 1:
            self.flows_viewer.show_flows()

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
        self.status_button.clicked.connect(self.show_panel)
        # flow button connect to flow viewer
        self.flow_button.clicked.connect(self.show_panel)
        # flow control button
        self.flow_control.clicked.connect(self.show_panel)

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
                self.Info_present_window.switch_ids.clear()
                self.flows_viewer.flow_switch_ids.clear()
                self.flow_control_window_present.switch_id_flow.clear()
                for switch in switches:
                    self.Info_present_window.switch_ids.addItem(switch)
                    self.flows_viewer.flow_switch_ids.addItem("SW_" + switch)
                    self.flow_control_window_present.switch_id_flow.addItem(
                        "SW_" + switch)
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
        # operation
        matches, self.match_value = read_json_(path="data/matches.json")
        actions, self.actions_value = read_json_(path="data/actions.json")
        self.match_field.addItems(matches)
        self.action_type_apply.addItems(actions)
        self.action_type_write_action.addItems(actions)
        self.match_field.activated.connect(self.match_value_find)
        self.action_type_apply.activated.connect(
            self.action_type_apply_value_find)
        self.action_type_write_action.activated.connect(
            self.action_type_write_action_value_find)

    def action_type_write_action_value_find(self, item):
        self.value_write_action.setPlaceholderText(self.actions_value[item])

    def action_type_apply_value_find(self, item):
        self.value_apply_action.setPlaceholderText(self.actions_value[item])

    def match_value_find(self, item):
        self.value_match_field.setPlaceholderText(self.match_value[item])

    def submit_button(self):
        """
        submit request with current form.
        :return:
        """
        data = {}
        id = self.switch_id_flow.currentText()
        if id != '':
            data["dpid"] = int(id[3:])
            data["operation"] = self.operation
            data["table_id"] = self.table_id_flow.value()

            data["priority"] = check_to_line_edit(
                self.priority)
            data["idle_timeout"] = check_to_line_edit(
                self.idle_timeout)
            data["hard_timeout"] = check_to_line_edit(
                self.hard_timeout)
            data["cookie"] = check_to_line_edit(self.cookie)
            data["cookie_mask"] = check_to_line_edit(
                self.cookie_mask)
            data["out_port"] = check_to_line_edit(
                self.output_port)
            data["out_group"] = check_to_line_edit(
                self.output_group)
            data["meter_id"] = check_to_line_edit(
                self.meter_id)
            data["metadata"] = check_to_line_edit(
                self.write_metadate)
            data["metadata_mask"] = check_to_line_edit(
                self.metadate_mask)
            data["goto"] = check_to_line_edit(self.goto_table)

            data["matchcheckbox"] = self.match_any.isChecked()
            data["clearactions"] = self.clear_actions.isChecked(
            )
            data["SEND_FLOW_REM"] = self.send_flowremoved_msg.isChecked(
            )
            data["CHECK_OVERLAP"] = self.check_overlapping.isChecked(
            )
            data["RESET_COUNTS"] = self.reset_counts.isChecked(
            )
            data["NO_PKT_COUNTS"] = self.do_not_count_packets.isChecked(
            )
            data["NO_BYT_COUNTS"] = self.do_not_count_bytes.isChecked(
            )

            data["apply"] = []

            if self.match_field.currentText() != '':
                data["match"] = {
                    self.match_field.currentText(): self.value_match_field.text()}
            else:
                data["match"] = {}

            if self.action_type_apply.currentText() != '':
                data["apply"].append(
                    {self.action_type_apply.currentText(): self.value_apply_action.text()})

            if self.action_type_write_action.currentText() != '':
                data["write"] = {
                    self.action_type_write_action.currentText(): self.value_write_action.text()}
            else:
                data["write"] = {}

            response = main_ui.cache.post_flow_control(
                up_key="control", data=data)
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


class flow_present_window(QMainWindow, Ui_flow):

    def __init__(self):
        super(flow_present_window, self).__init__()
        self.setupUi(self)
        # view
        self.flow_table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.flow_table_view.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.flow_table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flow_table_view.setStyleSheet(
            "QHeaderView::section{Background-color:rgb(0,1,1)}")

        self.flow_table_view.resizeColumnsToContents()
        self.flow_table_view.resizeRowsToContents()
        self.flow_table_view.horizontalScrollBar()
        self.flow_table_view.verticalHeader().setVisible(False)
        self.flow_table_view.itemClicked.connect(self.current_item)

        self.flow_switch_ids.activated.connect(self.show_flows)
        self.delete_flow.clicked.connect(self.delete_flow_function)
        #
        self.highlight_item = -1
        self.flows = {}

    def delete_flow_function(self):
        if self.highlight_item != -1:
            data = []
            temp = self.flows[self.highlight_item].copy()
            temp["dpid"] = self.flow_switch_ids.currentText()[3:]
            data.append(temp)
            response = main_ui.cache.post_flow_control(
                up_key="flow_delete", data=data)
            if response.status_code == 200:
                QMessageBox.about(None, "Done!!",
                                  "Message sent successfully")
                self.show_flows()
                self.highlight_item = -1
            else:
                QMessageBox.about(None, "Warning",
                                  "Message sent failed")
        else:
            QMessageBox.about(None, "No item selected",
                              "Please select row item first")

    def current_item(self, item):
        self.highlight_item = item.row()

    def show_flows(self):
        id = self.flow_switch_ids.currentText()[3:]
        if main_ui.cache is not None:
            self.flows = get_info_by_keys(
                main_ui.cache, up_key="flows", switch_id=id)[str(id)]
            temp = []
            if len(self.flows) != 0:
                for key in self.flows[0].keys():
                    if key != "actions" and key != "match":
                        temp.append(key)
                temp = temp[-1:] + temp[:10]
                self.flow_table_view.setRowCount(len(self.flows))
                self.flow_table_view.setColumnCount(11)
                self.flow_table_view.setHorizontalHeaderLabels(temp)

                for i, data in enumerate(self.flows):
                    for j, value in enumerate(data):
                        if j <= 10:
                            newItem = QTableWidgetItem(str(data[temp[j]]))
                            self.flow_table_view.setItem(i, j, newItem)
            else:
                self.flow_table_view.clearContents()

                # self.flow_table_view.setModel(custom_model(flows[str(id)]))
        else:
            QMessageBox.about(None, "No sever Info",
                              "Please connect available server first")

    def close(self):
        self.hide()


class Info_present_window(QMainWindow, Ui_info_present):

    def __init__(self):
        super(Info_present_window, self).__init__()
        self.setupUi(self)
        # view
        self.port_desc.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.port_status.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.flow_summary.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_status.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.port_desc.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.port_desc.verticalHeader().setVisible(False)
        self.port_desc.setStyleSheet(
            "QHeaderView::section{Background-color:rgb(0,1,1)}")

        self.port_status.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.port_status.verticalHeader().setVisible(False)
        self.port_status.setStyleSheet(
            "QHeaderView::section{Background-color:rgb(0,1,1)}")

        self.flow_summary.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.flow_summary.verticalHeader().setVisible(False)
        self.flow_summary.setStyleSheet(
            "QHeaderView::section{Background-color:rgb(0,1,1)}")

        self.table_status.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_status.verticalHeader().setVisible(False)
        self.table_status.setStyleSheet(
            "QHeaderView::section{Background-color:rgb(0,1,1)}")

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
