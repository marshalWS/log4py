import logging

from src.logger import Logger


class Warn(Logger):
    def __init__(self, file_path):
        Logger.__init__(self, file_path, logging.WARN)

    def warn(self, message):
        self.logger.warn(self.package_name + self.pointer + message)

