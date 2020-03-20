#!/home/{username}/anaconda3 python
# encoding: utf-8
"""
@author: gaopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: gaopengbai0121@gmail.com
@software: garner
@file: sqlite_database.py
@time: 3/19/20 2:14 PM
@desc:
"""
import os
import sqlite3


class Database:
    """
    sqlite3 database operation
    """

    def __init__(self, path="../flow.db"):
        self.path = path
        if not os.path.isfile(path):
            self.create_db()

    def create_db(self):
        """
        create OPENFLOWS table of database if file not exist.
        :return:
        """
        conn = sqlite3.connect(self.path)
        # no matter the table is exist or not
        # conn.execute("DROP TABLE OPENFLOWS; ")
        conn.execute('''CREATE TABLE IF NOT EXISTS OPENFLOWS
                     (switch_ids  TEXT PRIMARY KEY      NOT NULL,
                      switch_desc TEXT,
                      port_desc   TEXT,
                      port_status  TEXT,
                      flow_summary TEXT,
                      table_status TEXT);''')
        conn.commit()
        conn.close()

    def insert_db(self, s, sd, pd, ps, fs, ts):
        """
        insert new data into OPENFLOWS table of database
        :param s: value of switch_ids
        :param sd: value of switch_desc
        :param pd: value of port_desc
        :param ps: value of port_status
        :param fs: value of flow_summary
        :param ts: value of table_status
        :return:
        """
        conn = sqlite3.connect(self.path)
        sql = ''' insert into OPENFLOWS
                  (switch_ids, switch_desc, port_desc, port_status, flow_summary, table_status)
                  values
                  (:s, :sd, :pd, :ps, :fs, :ts)'''

        conn.execute(sql, {'s': s, 'sd': sd, 'pd': pd,
                           'ps': ps, 'fs': fs, 'ts': ts})
        conn.commit()
        conn.close()

    def read_db(self):
        """
        read all data from OPENFLOWS table
        :return:
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.execute("SELECT * from OPENFLOWS")
        for row in cursor:
            print("switch_ids:" + row[0])
            print("switch_desc:" + row[1])
            print("port_desc:" + row[2])
            print("port_status:" + row[3])
            print("flow_summary:" + row[4])
            print("table_status:" + row[5])
        conn.close()

    def update_db(self, up_key, value, switch_id):
        """
        replace old value to value of up_key (item) depend on switch_id
        :param up_key: the item to be operated
        :param value: new data
        :param switch_id: ids
        :return:
        """
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        if up_key == "switch_desc":
            c.execute(
                'UPDATE OPENFLOWS set switch_desc = ? WHERE switch_ids= ?', (value, switch_id))
        elif up_key == "port_desc":
            c.execute(
                'UPDATE OPENFLOWS set port_desc = ? WHERE switch_ids= ?', (value, switch_id))
        elif up_key == "port_status":
            c.execute(
                'UPDATE OPENFLOWS set port_status = ? WHERE switch_ids= ?', (value, switch_id))
        elif up_key == "flow_summary":
            c.execute(
                'UPDATE OPENFLOWS set flow_summary = ? WHERE switch_ids= ?',
                (value,
                 switch_id))
        elif up_key == "table_status":
            c.execute(
                'UPDATE OPENFLOWS set table_status = ? WHERE switch_ids= ?',
                (value,
                 switch_id))
        conn.commit()
        conn.close()

    def check_db(self, up_key, switch_id):
        """
        check the value of up_key (item) depend on switch_id
        :param up_key: item
        :param switch_id: ids
        :return:
        """
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        if up_key == "switch_desc":
            results = c.execute(
                "SELECT switch_desc from OPENFLOWS WHERE switch_ids= ?",
                switch_id)
        elif up_key == "port_desc":
            results = c.execute(
                "SELECT port_desc from OPENFLOWS WHERE switch_ids= ?",
                switch_id)
        elif up_key == "port_status":
            results = c.execute(
                "SELECT port_status from OPENFLOWS WHERE switch_ids= ?",
                switch_id)
        elif up_key == "flow_summary":
            results = c.execute(
                "SELECT flow_summary from OPENFLOWS WHERE switch_ids= ?",
                switch_id)
        elif up_key == "table_status":
            results = c.execute(
                "SELECT table_status from OPENFLOWS WHERE switch_ids= ?",
                switch_id)
        for row in results:
            print(row)
        conn.close()

    def delete_db(self, switch_id):
        """
        delete sheet
        :param switch_id:
        :return:
        """
        conn = sqlite3.connect(self.path)
        conn.execute("DELETE from OPENFLOWS where switch_ids= ?", switch_id)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    a = Database()
    # a.insert_db("2", "ha", "ga", "ma", "ka", "ta")
    # a.update_db("port_status", "yes", "2")
    # a.check_db("port_status", "2")
    a.delete_db("2")
