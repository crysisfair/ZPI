#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import configparser
import getpass


class ConfigHelper:
    def CreateFile(self):
        try:
            # self.conf.read(self.config_file)
            self.conf.add_section("db")
            self.conf.set("db", "user", "zpi_db")
            self.conf.set("db", "passwd", "123456")
            self.conf.add_section("email")
            self.conf.set("email", "user", "test@sample.com")
            self.conf.set("email", "passwd", "zpi_test")
            self.conf.add_section("log")
            self.conf.set("log", "enable", "yes")
            self.conf.set("log", "level", "warning")
            self.conf.set("log", "file", "/tmp/zpi.log")
            # self.conf.set("log", "format", "%(asctime)s [%(levelname)s] %(message)s")
            with open(self.config_file, 'w') as f:
                self.conf.write(f)
        except Exception as e:
            print(e)

    def Init(self):
        self.user_name = getpass.getuser()
        self.home = os.path.expandvars('$HOME')
        self.dir_name = self.home + r'/.zpi'
        self.config_file = self.dir_name + r'/zpi.conf'
        # print(self.config_file)
        if os.path.exists(self.dir_name) == False:
            os.makedirs(self.dir_name)
        if os.path.exists(self.config_file) == False:
            print("No such config file, now will create it.")
            self.CreateFile()

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.Init()

    def GetConfig(self, section, option):
        try:
            self.conf.read(self.config_file)
            if self.conf.has_option(section, option):
                return self.conf.get(section, option)
            else:
                return "No such config " + section + " " + option
        except Exception as e:
            print(e)
