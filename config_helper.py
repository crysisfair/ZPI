#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import ConfigParser
import getpass

class ConfigHelper:
    def __init__(self):
        print("Config init")
        self.conf = ConfigParser.ConfigParse()

    def Init(self):
        self.user_name = getpass.getuser()
        self.home = os.path.expandvars('$HOME')
        self.dir_name = self.home + r'/.zpi'
        self.config_file = self.dir_name + r'/zpi.conf'
        if os.path.exists(self.dir_name) == False:

    def CreateFile(self):
        try:
            os.makedir(self.dir_name)
            conf.read(self.config_file)
            conf.add_section("database")
        except Exception as e:
            print(e)
