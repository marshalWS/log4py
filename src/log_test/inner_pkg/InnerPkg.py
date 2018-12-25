import threading

from src.log_test.T1 import T1
from src.log_test.T2 import T2
from src.logger_factory import LoggerFactory


class InnerPkg:
    def __init__(self):
        self.logger = LoggerFactory("InnerPkg.class")
        t1 = T1()
        t2 = T2()

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
    innerPkg = InnerPkg()
    innerPkg.test()
    pass
