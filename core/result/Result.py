# @Author   :zhenqiang.wang
# @Time     :2023/6/14 16:41
#

from common.ResultEventType import *


class Result:

    def __init__(self):
        self.data = None
        self.msg = None
        self.code = None
        self.total = None

    def success(self, msg, data=None, total=None):
        self.code = RESPONSE_CODE.SUCCESS.value
        self.msg = msg
        self.data = data
        self.total = total
        return self

    def fail(self, msg):
        self.code = RESPONSE_CODE.FAIL.value
        self.msg = msg
        return self
