import logging

from src.logger import Logger


class Warn(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.WARN)

    def warn(self, message):
        self.logger.warn(self.class_name + self.pointer + message)
