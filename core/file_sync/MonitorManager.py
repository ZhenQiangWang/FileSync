# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 文件监控管理器

from datetime import datetime
from common.LogUtils import LogUtils
from core.file_sync.utils.CheckRulesUtil import *
from core.file_sync.FileMonitor import Monitor
from core.file_sync.FileSyncEventType import MonitorStatus, MonitorConfigStatus

log = LogUtils.log


# 单例模式
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class MonitorManager:
    # monitorManager = None

    def __init__(self):
        self.observers = {}

    # 初始化加载配置，启动监控
    def initialize(self):
        try:
            configs = get_all_active_config()
            for document in configs:
                monitor_id = document['_id']
                monitor_path = document['monitor_path']
                target_path = document['target_path']
                rules = document['rules']
                recursive = document['recursive']
                is_running = document['is_running']
                monitor = Monitor(monitor_id, monitor_path, target_path, rules, recursive)
                self.observers[monitor_id] = monitor
                log.info('初始化加载。。。监控注册成功，监控路径：%s，目标路径：%s，规则定义：%s', monitor_path, target_path, rules)
                if is_running == MonitorStatus.RUNNING.value:
                    monitor.start_monitor()
                log.info('初始化注册监听成功')
        except Exception as ex:
            raise ex

    # 获取所有监控配置
    def get_all_monitor(self, page_number, page_size):
        configs = get_all_active_config(page_number, page_size)
        return list(configs)

    def get_all_config_count(self):
        return get_config_count()

    def get_monitor_by_id(self, monitor_id):
        configs = get_active_by_monitor_id(monitor_id)
        return configs.next()

    # 创建监控
    def create(self, monitor_path, event_handler, recursive):
        try:
            target_path = event_handler.target_path
            rules = event_handler.rules
            if get_active_count_by_monitor_path(monitor_path) > 0:
                raise FileMonitorException("该监控目录已添加过:{}".format(monitor_path))
            # 规则校验
            check(monitor_path, target_path, recursive, rules)
            file_sync_config = {
                'monitor_path': monitor_path,
                'target_path': target_path,
                'rules': rules,
                'recursive': recursive,
                'is_running': MonitorStatus.STOP.value,
                'is_delete': MonitorConfigStatus.ACTIVE.value,
                'modify_time': datetime.now()
            }
            monitor_id = insert_config(file_sync_config)
            monitor = Monitor(monitor_id, monitor_path, target_path, rules, recursive)
            # monitor.start_monitor()
            # 监听注册
            self.observers[str(monitor_id)] = monitor
            log.info('监控创建成功，监控路径：%s，目标路径：%s，规则定义：%s', monitor_path, target_path, rules)
        except Exception as ex:
            raise ex

    # 开启监听
    def start(self, monitor_id):
        try:
            monitor = self.observers[monitor_id]
            monitor.stop_monitor()
            new_monitor = Monitor(monitor_id, monitor.monitor_path, monitor.target_path, monitor.rules,
                                  monitor.recursive)
            new_monitor.start_monitor()
            self.observers[monitor_id] = new_monitor
            update_config({'_id': ObjectId(monitor_id)}, {'is_running': MonitorStatus.RUNNING.value})
        except Exception as ex:
            raise ex

    # 更新配置
    def update(self, monitor_id, monitor_path, target_path, rules, recursive):
        try:
            check(monitor_path, target_path, recursive, rules)
            monitor = self.observers[monitor_id]
            monitor.stop_monitor()
            new_monitor = Monitor(monitor_id, monitor_path, target_path, rules, recursive)
            update_config({'_id': ObjectId(monitor_id)}, {
                'monitor_path': monitor_path,
                'target_path': target_path,
                'rules': rules,
                'recursive': recursive,
                'is_running': MonitorStatus.STOP.value,
                'is_delete': MonitorConfigStatus.ACTIVE.value,
                'modify_time': datetime.now()
            })
            self.observers[monitor_id] = new_monitor
        except Exception as ex:
            raise ex

    # 移除监控
    def remove(self, monitor_id):
        try:
            monitor = self.observers[monitor_id]
            monitor.stop_monitor()
            del_config({'_id': ObjectId(monitor_id)})
            log.info('监控移除成功')
        except Exception as ex:
            raise ex

    # 暂停监控
    def stop(self, monitor_id):
        try:
            monitor = self.observers[monitor_id]
            monitor.stop_monitor()
            update_config({'_id': ObjectId(monitor_id)}, {'is_running': MonitorStatus.STOP.value})
        except Exception as ex:
            raise ex

    # 停止所有监控
    def stop_all(self):
        try:
            for monitor_id, monitor in self.observers.items():
                monitor.stop(monitor_id)
                log.info('项目停止前停止，监控停止成功，监控路径：%s，目标路径：%s，规则定义：%s', monitor.monitor_path, monitor.target_path,
                         monitor.rules)
        except Exception as ex:
            raise ex
