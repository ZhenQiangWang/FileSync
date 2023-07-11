# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:09
# 同步日志
from common.MongoDBUtils import MongoDBUtils
import config


# 保存同步日志
def save_sync_log(sync_log):
    MongoDBUtils.get_collection(config.MONGODB_SYNC_LOG_COLLECTION).insert_one(sync_log)


# 获取文件所有同步日志
def get_all_log(page_number, page_size):
    # 分页查询参数
    pipeline = [
        {'$addFields': {'_id': {'$toString': '$_id'}}},
        # 分页
        {"$skip": (page_number - 1) * page_size},
        {"$limit": page_size}
    ]
    page_size = 10  # 每页文档数量
    page_number = 1  # 当前页码
    return MongoDBUtils.get_collection(config.MONGODB_SYNC_LOG_COLLECTION).aggregate(pipeline)


# 根据文件名获取同步日志
def get_sync_log_by_file_name(file_name):
    pipeline = [
        {'$match': {'file_name': file_name, 'is_delete': 0}},
        {'$addFields': {'_id': {'$toString': '$_id'}}}
    ]
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_LOG_COLLECTION)
    return collection.aggregate(pipeline)


# 根据ID获取同步日志
def get_sync_log_by_monitor_id(page_number, page_size, monitor_id):
    # 分页查询参数
    pipeline = [
        {'$match': {'monitor_id': monitor_id}},
        {
            '$addFields': {
                '_id': {'$toString': '$_id'},
                'modify_time': {
                    '$dateToString': {
                        'date': '$modify_time',
                        'format': '%Y-%m-%d %H:%M:%S'
                    }
                }
            }
        },
        {'$sort': {'modify_time': -1}},
        # 分页
        {"$skip": (page_number - 1) * page_size},
        {"$limit": page_size},

    ]
    return MongoDBUtils.get_collection(config.MONGODB_SYNC_LOG_COLLECTION).aggregate(pipeline)


def get_sync_log_count_by_monitor_id(monitor_id):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_LOG_COLLECTION)
    return collection.count_documents({'monitor_id': monitor_id})
