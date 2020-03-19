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


def get_info(ip, port):

    url = "http://"+ip+":"+port+"/data?switchdesc=1"

    try:
        r = requests.get(url)

    except ConnectionError as e:  # This is the correct syntax
        print(e)
        r = "no response"
    return r
