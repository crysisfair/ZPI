#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from config_helper import ConfigHelper

cfg = ConfigHelper()
username = cfg.GetConfig("email", "passwd")
print(username)

