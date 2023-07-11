# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:43
#
import traceback
from flask import Blueprint
from flask import request, jsonify

from core.result.Result import Result
from router import fileConfigRouter
from router import fileSyncRouter
from common.LogUtils import LogUtils

log = LogUtils.log

# 定义蓝图
file_monitor_config = Blueprint('file_monitor_config', __name__)


# 获取所有配置
@file_monitor_config.route("/fileSync/get_all_monitor", methods=["POST"])
def get_all_monitor():
    try:
        json = request.json
        page_number = json['page_number']
        page_size = json['page_size']
        result, total = fileConfigRouter.get_all_monitor(page_number, page_size)

        return jsonify(Result().success('获取成功', result, total).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 根据ID获取配置
@file_monitor_config.route("/fileSync/get_monitor_by_id", methods=["GET"])
def get_monitor_by_id():
    try:
        monitor_id = request.args['monitor_id']
        result = fileConfigRouter.get_monitor_by_id(monitor_id)
        return jsonify(Result().success('获取成功', result).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        Result().fail(str(ex))
        return jsonify(Result().fail(str(ex)).__dict__)


# 新增路径监控
@file_monitor_config.route("/fileSync/add_monitor", methods=["POST"])
def add_monitor():
    try:
        json = request.json
        monitor_path = json["monitor_path"]
        target_path = json["target_path"]
        recursive = bool(json["recursive"])
        rule = json["rules"]
        fileConfigRouter.add_monitor(monitor_path, target_path, rule, recursive)
        return jsonify(Result().success('新建成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 开启路径监控
@file_monitor_config.route("/fileSync/start_monitor", methods=["GET"])
def start_monitor():
    try:
        monitor_id = request.args["monitor_id"]
        fileConfigRouter.start_monitor(monitor_id)
        return jsonify(Result().success('启动成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 更新路径监控
@file_monitor_config.route("/fileSync/update_monitor", methods=["POST"])
def update_monitor():
    try:
        json = request.json
        monitor_id = json['_id']
        monitor_path = json["monitor_path"]
        target_path = json["target_path"]
        recursive = bool(json["recursive"])
        rules = json["rules"]
        fileConfigRouter.update_monitor(monitor_id, monitor_path, target_path, rules, recursive)
        return jsonify(Result().success('更新成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 移除指定监控
@file_monitor_config.route("/fileSync/remove_monitor", methods=["GET"])
def remove_monitor():
    try:
        monitor_id = request.args["monitor_id"]
        fileConfigRouter.remove_monitor(monitor_id)
        return jsonify(Result().success('移除成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 停止指定监控
@file_monitor_config.route("/fileSync/stop_monitor", methods=["GET"])
def stop_monitor():
    try:
        monitor_id = request.args["monitor_id"]
        fileConfigRouter.stop_monitor(monitor_id)
        return jsonify(Result().success('停止成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 获取所有同步log
@file_monitor_config.route("/fileSync/get_sync_log", methods=["GET"])
def get_all_sync_log():
    try:
        page_number = request.args['page_number']
        page_size = request.args['page_size']
        result = fileSyncRouter.get_all_sync_log(page_number, page_size)
        return jsonify(Result().success('查询成功', result).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)


# 根据监控Id获取同步log
@file_monitor_config.route("/fileSync/get_sync_log_by_monitor_id", methods=["POST"])
def get_sync_log_by_id():
    try:
        json = request.json
        monitor_id = json['monitor_id']
        page_number = json['page_number']
        page_size = json['page_size']
        total, result = fileSyncRouter.get_sync_log_by_id(page_number, page_size, monitor_id)
        return jsonify(Result().success('查询成功', result, total).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        return jsonify(Result().fail(str(ex)).__dict__)
