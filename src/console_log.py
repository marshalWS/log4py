# coding:utf-8
import logging
import time
import datetime
import os
import colorlog  # 日志颜色

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class ConsoleLog:
    def __init__(self):

        self.logger = logging.getLogger()
        # 指定最低输出级别
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(

            '%(log_color)s[%(asctime)s]  [%(levelname)s]- %(message)s',

            # '%(log_color)s [%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S',

            log_colors=log_colors_config)  # 日志输出格式

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def __console(self, level, message):

        # 创建一个StreamHandler,用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    log = ConsoleLog()
    log.debug("---测试开始----")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")
    log.error("----测试结束----")
