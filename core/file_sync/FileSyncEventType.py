# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 文件操作枚举
from enum import Enum


# 文件操作状态
class FileSyncEventType(Enum):
    RENAME = 1
    MODIFY = 2
    DELETE = 3
    IGNORE = 4


# 监控状态
class MonitorStatus(Enum):
    STOP = 0
    RUNNING = 1


# 监控配置状态
class MonitorConfigStatus(Enum):
    ACTIVE = 0
    DELETE = 1
