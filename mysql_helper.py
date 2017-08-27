#! /usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb


class MySQLHelper:

    def __init__(self, log, host, user, password, charset="utf8"):
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset
        self.log=log
        try:
            self.conn=MySQLdb.connect(host=self.host, user=self.user, passwd=self.password)
            self.conn.set_character_set(self.charset)
            self.cur=self.conn.cursor()
            self.log.info("Mysql init complete")
        except MySQLdb.Error as e:
            self.log.error("Mysql Error {0}: {1}".format(e.args[0], e.args[1]))
            # print()"Mysql Error %d: %s" % (e.args[0], e.args[1])

    def selectDb(self, db):
        try:
            self.conn.select_db(db)
        except MySQLdb.Error as e:
            self.log.error("Mysql Error {0}: {1}".format(e.args[0], e.args[1]))
            # print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self, sql):
        try:
            n=self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            self.log.error("Mysql Error:{0}\n SQL: {1}".format(e, sql))
            # print("Mysql Error:%s\nSQL:%s" %(e, sql))

    def queryRow(self, sql):
        self.query(sql)
        result = self.cur.fetchone()
        return result

    def queryAll(self, sql):
        self.query(sql)
        result=self.cur.fetchall()
        desc =self.cur.description
        d = []
        for inv in result:
            d = {}
            for i in range(0, len(inv)):
                d[desc[i][0]] = str(inv[i])
            d.append(d)
        return d

    def insert(self, p_table_name, p_data):
        for key in p_data:
            p_data[key] = "'""'" + str(p_data[key]) + "'"
        key = ','.join(p_data.keys())
        value = ','.join(p_data.values())
        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value + ")"
        # self.query("set names 'utf8'")
        return self.query(real_sql)

    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
