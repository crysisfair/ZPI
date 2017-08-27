#! /usr/bin/python3
# -*- coding: utf-8 -*-

from mysql_helper import MySQLHelper

class MailPersistor:

    def __init__(self, log, config):
        self.log = log
        self.config = config
        self.db_helper = MySQLHelper(log=log, host="localhost", user=config["db_user"], password=config["db_passwd"])
        self.db_helper.query("""create database if not exists zpi""")
        self.db_helper.selectDb(config["zpi"])
