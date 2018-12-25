import os
from os import path
from xml.dom.minidom import parse
import xml.dom.minidom


class LoggingXmlParser:
    cur_path = path.dirname(__file__)
    path = cur_path + "\logging.xml"

    pass


def log_max_size_config(default_m=3):
    DOMTree = xml.dom.minidom.parse(LoggingXmlParser.path)
    collection = DOMTree.documentElement

    loggings = collection.getElementsByTagName("logging")
    for log in loggings:
        if log.hasAttribute("title"):

            try:
                log_file_min_size = log.getElementsByTagName('max_size_m')[0]
                return int(log_file_min_size.childNodes[0].data)
            except:
                return default_m
    return default_m


def log_backup_count(default_count=5):
    DOMTree = xml.dom.minidom.parse(LoggingXmlParser.path)
    collection = DOMTree.documentElement

    loggings = collection.getElementsByTagName("logging")
    for log in loggings:
        if log.hasAttribute("title"):

            try:
                log_file_min_size = log.getElementsByTagName('backup_count')[0]
                return int(log_file_min_size.childNodes[0].data)
            except:
                return default_count
    return default_count


def level_config(default="NOTSET"):
    DOMTree = xml.dom.minidom.parse(LoggingXmlParser.path)
    collection = DOMTree.documentElement
    loggings = collection.getElementsByTagName("logging")
    for log in loggings:
        if log.hasAttribute("title"):
            try:
                level = log.getElementsByTagName('level')[0]
                return level.childNodes[0].data.upper()
            except:
                return default
    return default


if __name__ == "__main__":
    # level_config = level_config()
    # print("level_config = ", level_config)
    #
    # ee = log_max_size_config()
    # print("ee = ", ee)

    pass
