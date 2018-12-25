import logging

from src.logger import Logger


class Error(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.ERROR)

    def error(self, message):
        self.logger.error(self.class_name + self.pointer + message)
