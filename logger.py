#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging


class Logger:
    def Init(self):
        ls = str.lower(self.levelstr)
        l = logging.WARNING
        if ls == "debug":
            l = logging.DEBUG
        elif ls == "info":
            l = logging.INFO
        elif ls == "warning":
            l = logging.WARNING
        elif ls == "error":
            l = logging.ERROR
        elif ls == "critical":
            l = logging.CRITICAL
        else:
            l = logging.WARNING
        self.level = l
        logging.basicConfig(level=l, format=self.log_format, datefmt='%a %d %b %Y %H:%M:%S', filename=self.file, filemode='a')
        # logging.basicConfig(level=l, datefmt='%a %d %b %Y %H:%M:%S', filename=self.file, filemode='a')

    def GetLogger(self):
        logger = logging.getLogger()
        logger.setLevel(self.level)
        fh = logging.FileHandler(self.file, "a")
        fh.setLevel(self.level)
        ch = logging.StreamHandler()
        ch.setLevel(self.level)
        fmt = logging.Formatter(self.log_format)
        fh.setFormatter(fmt)
        ch.setFormatter(fmt)
        # logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info("Log init complete")
        return logger

    def __init__(self, en, level, file):
        self.en = en
        self.levelstr = level
        self.log_format = "%(asctime)s [%(levelname)s] %(message)s"
        self.file = file
        self.Init()
