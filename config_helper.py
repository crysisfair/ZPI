#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import configparser
import getpass

class ConfigHelper:
    def CreateFile(self):
        try:
            #self.conf.read(self.config_file)
            self.conf.add_section("database")
            self.conf.set("database", "username", "zpi_db")
            self.conf.set("database", "passwd", "123456")
            self.conf.add_section("email")
            self.conf.set("email", "username", "test@sample.com")
            self.conf.set("email", "passwd", "zpi_test")
            with open(self.config_file, 'w+') as f:
                self.conf.write(f)
        except Exception as e:
            print(e)

    def Init(self):
        self.user_name = getpass.getuser()
        self.home = os.path.expandvars('$HOME')
        self.dir_name = self.home + r'/.zpi'
        self.config_file = self.dir_name + r'/zpi.conf'
        print(self.config_file)
        if os.path.exists(self.dir_name) == False:
            os.makedirs(self.dir_name)
        if os.path.exists(self.config_file) == False:
            self.CreateFile()

    def __init__(self):
        print("Config init")
        self.conf = configparser.ConfigParser()
        self.Init()


    def GetConfig(self, section, option):
        try:
            self.read(self.config_file)
            if self.conf.has_section(section) and self.conf.has_option(option):
                self.get(section, option)
            else:
                return "No such config " + section + " " +  option
        except Exception as e:
            print(e)

