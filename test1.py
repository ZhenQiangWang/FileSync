import time

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from pymongo import MongoClient
if __name__ == '__main__':
    # 连接MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['scheduler']  # MongoDB数据库名

    # 创建MongoDBJobStore
    jobstore = MongoDBJobStore(database='scheduler')

    # 创建调度器
    scheduler = BlockingScheduler(jobstores={'default': jobstore})

    def task1(x):
        print(f'task 1 executed --------: {x}', time.time())

    def task2(x):
        print(f'task 2 executed --------: {x}', time.time())

    # 添加定时任务
    scheduler.add_job(func=task1, args=('循环',), trigger='interval', seconds=5, replace_existing=True, id='interval_task')
    scheduler.add_job(func=task2, args=('定时任务',), trigger='cron', second='*/10', replace_existing=True, id='cron_task')

    # 启动调度器
    scheduler.start()
