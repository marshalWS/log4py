import logging

from src.logger import Logger


class Critical(Logger):
    def __init__(self, file_path):
        Logger.__init__(self, file_path, logging.CRITICAL)

    def critical(self, message):
        self.logger.critical(self.package_name + self.pointer + message)
