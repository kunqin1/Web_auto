import logging
import os

from Common.handle_config import conf
from Common.handle_path import logs_dir


class MyLogger(logging.Logger):
    """
    创建loggers（日志器）, handlers（处理器）和formatters（日志格式）并分别调用它们的配置函数
    """

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        # 继承日志器，并赋值
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道,创建一个流处理器handler并设置其日志格式
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        # 为日志器添加处理器handle1
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, conf.get("log", "file_name"))
else:
    file_name = None

logger = MyLogger(file_name)

