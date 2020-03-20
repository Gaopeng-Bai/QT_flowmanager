#!/home/{username}/anaconda3 python
# encoding: utf-8
"""
@author: gaopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: gaopengbai0121@gmail.com
@software: garner
@file: server_info.py
@time: 3/18/20 4:38 PM
@desc:
"""
import requests
from requests.exceptions import ConnectionError


class req_server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_info(self, key, ids):
        url = {
            "switch_ids": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?list=switches",
            "switch_desc": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?switchdesc=<dpid>",
            "port_desc": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?portdesc=<dpid>",
            "port_status": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?portstat=<dpid>",
            "flow_summary": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?flowsumm=<dpid>",
            "table_status": "http://" +
            self.ip +
            ":" +
            self.port +
            "/data?tablestat=<dpid>"}

        if key in url:
            if key == "switch_ids":
                req_url = url[key]
            else:
                req_url = url[key].replace("<dpid>", str(ids))
            try:
                r = requests.get(req_url)

            except ConnectionError as e:  # This is the correct syntax
                print(e)
                r = "no response"
            return r
        else:
            return 0

    def post_flow_control(self):
        url = "http://" + self.ip + ":" + self.port + "/flowform"
        payload = {
            "dpid": 1,
            "operation": "add",
            "table_id": 0,
            "priority": 0,
            "idle_timeout": 0,
            "hard_timeout": 0,
            "cookie": 0,
            "cookie_mask": 0,
            "out_port": 0,
            "out_group": 0,
            "meter_id": 0,
            "metadata": 0,
            "metadata_mask": 0,
            "goto": 0,
            "matchcheckbox": False,
            "clearactions": False,
            "SEND_FLOW_REM": False,
            "CHECK_OVERLAP": False,
            "RESET_COUNTS": False,
            "NO_PKT_COUNTS": False,
            "NO_BYT_COUNTS": False,
            "match": {},
            "apply": [],
            "write": {}
        }
        try:
            r = requests.post(url, data=payload)
        except ConnectionError as e:  # This is the correct syntax
            print(e)
            r = "no response"
        return r
