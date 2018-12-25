import logging


from src.logger import Logger


class Debug(Logger):
    def __init__(self, class_name, file_path):
        self.class_name = class_name
        Logger.__init__(self, file_path, logging.DEBUG)

    def debug(self, message):
        self.logger.debug(self.class_name + self.pointer + message)
