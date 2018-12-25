import logging

from src.logger import Logger


class Info(Logger):
    def __init__(self, file_path):
        Logger.__init__(self, file_path, logging.INFO)

    def info(self, message):
        self.logger.info(self.package_name + self.pointer + message)
