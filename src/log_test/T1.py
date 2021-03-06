import threading

from src.logger_factory import LoggerFactory


class T1:
    def __init__(self):
        self.logger = LoggerFactory("T1.class")

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
    t1 = T1()
    t1.test()
    pass
