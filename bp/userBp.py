# @Author   :zhenqiang.wang
# @Time     :2023/6/19 10:43
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
user_bp = Blueprint('user_bp', __name__)


# 登录
@user_bp.route("/user/login", methods=["POST"])
def login():
    try:
        json = request.json
        user_name = json['username']
        password = json['password']
        res = {'token': user_name}
        return jsonify(Result().success('获取成功', res).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        Result().fail(str(ex))
        return jsonify(Result().fail(str(ex)).__dict__)


# 登录
@user_bp.route("/user/logout", methods=["GET"])
def logout():
    try:
        return jsonify(Result().success('获取成功').__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        Result().fail(str(ex))
        return jsonify(Result().fail(str(ex)).__dict__)


@user_bp.route("/user/info", methods=["GET"])
def getinfo():
    try:
        res = {}
        roles = ['123']
        res['roles'] = roles
        res['name'] = 'super13'
        res['introduction'] = 'introduction'
        res['avatar'] = './assets/img/R-C.gif'
        return jsonify(Result().success('获取成功', res).__dict__)
    except Exception as ex:
        log.error(traceback.format_exc())
        Result().fail(str(ex))
        return jsonify(Result().fail(str(ex)).__dict__)
