import logging

from src.logger import Logger


class Critical(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.CRITICAL)

    def critical(self, message):
        self.logger.critical(self.class_name + self.pointer + message)
