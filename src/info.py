import logging

from src.logger import Logger


class Info(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.INFO)

    def info(self, message):
        self.logger.info(self.class_name + self.pointer + message)
