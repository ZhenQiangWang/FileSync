# @Author   :zhenqiang.wang
# @Time     :2023/6/15 13:34
#
from watchdog.observers import Observer
from common.MongoDBUtils import MongoDBUtils
from common.LogUtils import LogUtils
from core.file_sync.utils.CheckRulesUtil import *
from core.file_sync.BaseFileMonitor import BaseFileMonitor

log = LogUtils.log


# 监听类
class Monitor:
    def __init__(self, monitor_id, monitor_path, target_path, rules, recursive):
        self.observer = Observer()
        self.monitor_id = monitor_id
        self.monitor_path = monitor_path
        self.target_path = target_path
        self.rules = rules
        self.recursive = recursive

    # 启动监控
    def start_monitor(self):
        try:
            self.observer.schedule(BaseFileMonitor(self.monitor_path, self.target_path, self.rules, self.monitor_id), self.monitor_path, recursive=self.recursive)
            if not self.observer.is_alive():
                self.observer.start()
            log.info('监控启动成功，监控路径：%s，目标路径：%s，规则定义：%s', self.monitor_path, self.target_path, self.rules)
        except Exception as ex:
            raise ex

    def stop_monitor(self):
        try:
            if self.observer and self.observer.is_alive():
                self.observer.stop()
                self.observer.join()
            log.info('监控停止成功，监控路径：%s，目标路径：%s，规则定义：%s', self.monitor_path, self.target_path, self.rules)
        except Exception as ex:
            raise ex
