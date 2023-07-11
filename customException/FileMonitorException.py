# @Author   :zhenqiang.wang
# @Time     :2023/6/15 15:45
# 文件监控自定义异常

class FileMonitorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
