# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 项目主入口
from flask import Flask
from core.file_sync.MonitorManager import MonitorManager
from bp.fileMonitorBp import file_monitor_config
from bp.userBp import user_bp

app = Flask(__name__)
# 注册蓝图
app.register_blueprint(file_monitor_config)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    try:
        # app.run(debug=True)
        app.run()
    finally:
        MonitorManager().stop_all()
        print("项目停止")
