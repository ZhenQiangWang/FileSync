# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:42
# 文件监控配置

from core.file_sync.BaseFileMonitor import BaseFileMonitor
from core.file_sync.MonitorManager import MonitorManager
from common.LogUtils import LogUtils

log = LogUtils.log


# 获取所有监控
def get_all_monitor(page_number, page_size):
    try:
        infos = MonitorManager().get_all_monitor(page_number, page_size)
        total = MonitorManager().get_all_config_count()
        return infos, total
    except Exception as ex:
        raise ex


# 获取所有监控
def get_monitor_by_id(monitor_id):
    try:
        return MonitorManager().get_monitor_by_id(monitor_id)
    except Exception as ex:
        raise ex

# 新增监控
def add_monitor(monitor_path, target_path, rules, recursive):
    try:
        MonitorManager().create(monitor_path, BaseFileMonitor(monitor_path, target_path, rules), recursive)
    except Exception as ex:
        raise ex


# 开启监控
def start_monitor(monitor_id):
    try:
        MonitorManager().start(monitor_id)
    except Exception as ex:
        raise ex


# 修改监控
def update_monitor(monitor_id, monitor_path, target_path, rules, recursive):
    try:
        MonitorManager().update(monitor_id, monitor_path, target_path, rules, recursive)
    except Exception as ex:
        raise ex


# 移除监控
def remove_monitor(monitor_id):
    try:
        MonitorManager().remove(monitor_id)
    except Exception as ex:
        raise ex


# 暂停监控
def stop_monitor(monitor_id):
    try:
        MonitorManager().stop(monitor_id)
    except Exception as ex:
        raise ex
