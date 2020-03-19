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


def get_info(ip, port, key, id=0):
    url = {"switch_ids": "http://" + ip + ":" + port + "/data?list=switches",
           "switch_desc": "http://" + ip + ":" + port + "/data?switchdesc=<dpid>",
           "Port_Desc": "http://" + ip + ":" + port + "/data?portdesc=<dpid>",
           "port_status": "http://" + ip + ":" + port + "/data?portstat=<dpid>",
           "flow_summary": "http://" + ip + ":" + port + "/data?flowsumm=<dpid>",
           "table_status": "http://" + ip + ":" + port + "/data?tablestat=<dpid>"}

    if key in url:
        if key == "switch_ids":
            req_url = url[key]
        else:
            req_url = url[key].replace("<dpid>", str(id))
        try:
            r = requests.get(req_url)

        except ConnectionError as e:  # This is the correct syntax
            print(e)
            r = "no response"
        return r
    else:
        return 0
