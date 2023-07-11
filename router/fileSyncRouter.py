# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:42
# 文件同步日志配置

from core.file_sync.Repository.SyncLogRepository import *
from common.LogUtils import LogUtils

log = LogUtils.log


# 获取所有监控
def get_all_sync_log(page_number, page_size):
    try:
        return list(get_all_log(page_number, page_size))
    except Exception as ex:
        raise ex


def get_sync_log_by_id(page_number, page_size, monitor_id):
    try:
        lof_info = list(get_sync_log_by_monitor_id(page_number, page_size, monitor_id))
        total = get_sync_log_count_by_monitor_id(monitor_id)
        return total, lof_info
    except Exception as ex:
        raise ex
