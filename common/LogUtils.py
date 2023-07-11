# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 日志配置、记录工具类
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import colorama
from colorama import *
import os
import config


class LogUtils:
    log = None

    @staticmethod
    def initialize():
        if LogUtils.log is not None:
            return
        log_dir = config.LOG_DIR
        # 获取当前时间，用于生成日志文件名
        current_time = datetime.now()
        log_file_name = current_time.strftime("%Y-%m-%d") + ".sql"
        log_file_path = os.path.join(log_dir, log_file_name)
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')

        # 创建 TimedRotatingFileHandler 处理器
        handler = TimedRotatingFileHandler(log_file_path, when="midnight", backupCount=30)
        # console_handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # error_handler = TimedRotatingFileHandler(os.path.join(log_dir, 'error.sql'), when="midnight", backupCount=30)
        # error_handler.setLevel(logging.ERROR)
        # 初始化 colorama 库，启用控制台颜色支持
        colorama.init()

        # 定义日志级别与对应的颜色
        LOG_LEVEL_COLORS = {
            logging.DEBUG: Fore.WHITE,
            logging.INFO: Fore.WHITE,
            logging.WARNING: Fore.YELLOW,
            logging.ERROR: Fore.RED
        }

        # 定义自定义处理器类
        class ColoredConsoleHandler(logging.StreamHandler):
            def emit(self, record):
                level_color = LOG_LEVEL_COLORS.get(record.levelno, Fore.WHITE)
                colored_msg = f'{level_color}{self.format(record)}{Style.RESET_ALL}'
                print(colored_msg)

        # 创建自定义处理器实例
        colored_console_handler = ColoredConsoleHandler()
        colored_console_handler.setLevel(logging.DEBUG)

        handler.setFormatter(formatter)
        # console_handler.setFormatter(formatter)
        colored_console_handler.setFormatter(formatter)
        # error_handler.setFormatter(formatter)

        # 配置日志记录器
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # 将处理器添加到日志记录器
        logger.addHandler(handler)
        # logger.addHandler(console_handler)
        # 添加处理器到日志记录器
        logger.addHandler(colored_console_handler)
        # logger.addHandler(error_handler)
        LogUtils.log = logger
        print('日志配置初始化成功。。。')

    # 单例模式
    @staticmethod
    def getLog():
        if LogUtils.log is None:
            LogUtils.initialize()
        return LogUtils.log


