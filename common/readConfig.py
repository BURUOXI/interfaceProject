# -- coding: utf-8 --
from configparser import ConfigParser
import os

from interfaceProject.common.handlepath import CONFDIR


class HandleConfig:
    class HandleConfig(ConfigParser):

        def __init__(self, filename):
            # 调用父类的init方法
            super().__init__()
            self.filename = filename
            self.read(filename, encoding="utf8")

        def write_data(self, section, options, value):
            """写入数据的方法"""
            self.set(section, options, value)
            self.write(fp=open(self.filename, "w"))

    conf = HandleConfig(os.path.join(CONFDIR, "config.ini"))
