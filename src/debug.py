import logging


from src.logger import Logger


class Debug(Logger):
    def __init__(self, file_path):
        Logger.__init__(self, file_path, logging.DEBUG)

    def debug(self, message):
        self.logger.debug(self.package_name + self.pointer + message)
