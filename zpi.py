#! /usr/bin/python3
# -*- coding: utf-8 -*-

from config_helper import ConfigHelper
from logger import Logger


class Zpi:
    def LoadConfig(self):
        self.config = {}
        self.config['email_user'] = self.cfg.GetConfig("email", "user")
        self.config['email_passwd'] = self.cfg.GetConfig("email", "passwd")
        self.config['db_user'] = self.cfg.GetConfig("db", "user")
        self.config['db_passwd'] = self.cfg.GetConfig("db", "passwd")
        self.config['log_en'] = self.cfg.GetConfig("log", "enable")
        self.config['log_level'] = self.cfg.GetConfig("log", "level")
        self.config['log_file'] = self.cfg.GetConfig("log", "file")

    def Init(self):
        self.cfg = ConfigHelper()
        self.LoadConfig()
        logger = Logger(self.config["log_en"], self.config["log_level"], self.config["log_file"])
        self.log = logger.GetLogger()
        self.log.info("ZPI init complete.")

    def __init__(self):
        self.Init()
