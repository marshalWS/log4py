import threading

from src.logger_factory import LoggerFactory


class T2:
    def __init__(self):
        self.logger = LoggerFactory()

    def __run(self, i):
        self.logger.debug("debug " + str(i) + " -------------------")
        self.logger.info("info " + str(i) + " -------------------")
        self.logger.warn("warn " + str(i) + " -------------------")
        self.logger.error("error " + str(i) + " -------------------")
        self.logger.critical("critical " + str(i) + " -------------------")

    def test(self):
        for i in range(6):
            t = threading.Thread(target=self.__run, args=(i,))
            t.start()


if __name__ == '__main__':
    t2 = T2()
    t2.test()
    pass
