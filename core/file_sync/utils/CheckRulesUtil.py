# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:22
# 规则校验工具类

import os, time, sys
from datetime import datetime
from core.file_sync.Repository.SyncConfigRepository import *
from customException.FileMonitorException import FileMonitorException
from common.LogUtils import LogUtils
from flask import current_app

log = LogUtils.getLog()


# 根据临时文件的特征进行过滤
def is_rel_file(file_path):
    file_name = os.path.basename(file_path).upper()
    if '~$' in file_name:
        return False
    if not (file_name.endswith('CSV') or file_name.endswith('SWP') or
            file_name.endswith('S2P') or file_name.endswith('TXT') or
            file_name.endswith('STDF') or file_name.endswith('XLS') or
            file_name.endswith('XLSX')):
        return False
    return True


# 判断两个路径是否为子、父路径
def is_subdirectory(target_path, specified_path):
    pass
    # # 获取最长公共路径
    # common_path = os.path.commonprefix([target_path, specified_path])
    #
    # # 判断是否为子目录
    # if common_path == specified_path and target_path != specified_path:
    #     return True
    # else:
    #     return False

    # return target_path.startswith(specified_path)


# 新增/修改监控前校验
def check(add_monitor_path, target_path, add_recursive, rules):
    try:
        if not os.access(add_monitor_path, os.R_OK):
            raise FileMonitorException("该监控目录无权限访问或目录不存在：{}".format(add_monitor_path))
        if not os.access(target_path, os.R_OK):
            raise FileMonitorException("该目标目录无权限访问或目录不存在：{}".format(target_path))
        if not os.path.exists(add_monitor_path):
            raise FileMonitorException("该监控目录不存在：{}".format(add_monitor_path))
        if not os.path.exists(target_path):
            raise FileMonitorException("该目标目录不存在：{}".format(target_path))

        # 校验同步规则
        try:
            check_rules('test', rules,
                        os.path.join(os.path.join(current_app.root_path, 'static'), "新建 Microsoft Excel 工作表.xlsx"))
        except Exception as ex:
            raise FileMonitorException("该规则语法错误：{},{}".format(ex, rules))
        active_config = get_all_active_config()
        for document in active_config:
            monitor_path = document['monitor_path']
            recursive = document['recursive']
            # 判断添加的路径是否为查询出的路径的子目录
            # if is_subdirectory(add_monitor_path, monitor_path) and recursive:
            #     raise FileMonitorException(
            #         "本次添加目录：{},是历史设置监控路径：{}的子路径，且历史设置包含子目录，不可重复设置".format(add_monitor_path, monitor_path))
            # # 判断查询出的路径是否为添加的路径的子目录
            # elif is_subdirectory(monitor_path, add_monitor_path) and add_recursive:
            #     raise FileMonitorException(
            #         "历史设置监控路径：{},是本次添加目录：{}的子路径，且本次添加监控路径设置为包含子目录，不可重复设置".format(monitor_path, add_monitor_path))
    except Exception as ex:
        raise ex


def check_rules(monitor_id ,rules, file_path):
    try:
        if rules is None or rules == '':
            return True
        result = eval(rules)
        log.warning('ID:%s,规则校验，%s，%s,校验结果:%s',monitor_id, rules, file_path, result)
        return not result
    except Exception as ex:
        raise ex
