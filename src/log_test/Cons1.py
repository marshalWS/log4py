import threading

from src.console_log import ConsoleLog


def fun():
    log = ConsoleLog()
    log.debug("---测试开始------")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")
    log.error("----测试结束----")


if __name__ == "__main__":

    for i in range(6):
        t = threading.Thread(target=fun, args=())
        t.start()
