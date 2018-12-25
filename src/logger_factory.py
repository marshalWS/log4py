'''  所有 log 方法'''
import os
from os import path
from src.critical import Critical
from src.debug import Debug
from src.error import Error
from src.info import Info
from src.warn import Warn


class LoggerFactory:
    log_dir = None

    def __init__(self):
        if LoggerFactory.log_dir is None:
            cur_path = path.dirname(__file__)
            parent_path = os.path.dirname(cur_path)  # 获得d所在的目录,即d的父级目录
            LoggerFactory.log_dir = parent_path + "/logs"

        self.debug_path = LoggerFactory.log_dir + "/debug.log"
        self.info_path = LoggerFactory.log_dir + "/info.log"
        self.warn_path = LoggerFactory.log_dir + "/warn.log"
        self.error_path = LoggerFactory.log_dir + "/error.log"
        self.critical_path = LoggerFactory.log_dir + "/critical.log"

        self.__debug = Debug(self.debug_path)
        self.__info = Info(self.info_path)
        self.__warn = Warn(self.warn_path)
        self.__error = Error(self.error_path)
        self.__critical = Critical(self.critical_path)

    def debug(self, msg):
        self.__debug.debug(msg)

    def info(self, msg):
        self.__info.info(msg)

    def warn(self, msg):
        self.__warn.warn(msg)

    def error(self, msg):
        self.__error.error(msg)

    def critical(self, msg):
        self.__critical.critical(msg)