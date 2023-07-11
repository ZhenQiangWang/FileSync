from pymongo import MongoClient
import config
from common.LogUtils import LogUtils
# 获取日志记录器
log = LogUtils.getLog()


class MongoDBUtils:
    db = None

    @staticmethod
    def initialize():
        client = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
        MongoDBUtils.db = client[config.MONGODB_DATABASE]
        log.info("MongoDb初始化完成")

    @staticmethod
    def get_collection(collection_name):
        return MongoDBUtils.db[collection_name]
