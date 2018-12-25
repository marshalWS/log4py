import logging

from src.logger import Logger


class Error(Logger):
    def __init__(self, file_path):
        Logger.__init__(self, file_path, logging.ERROR)

    def error(self, message):
        self.logger.error(self.package_name + self.pointer + message)
