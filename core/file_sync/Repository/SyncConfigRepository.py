# @Author   :zhenqiang.wang
# @Time     :2023/6/15 10:08
# 监控配置配置针对DB操作
from common.MongoDBUtils import MongoDBUtils
import config
from bson.objectid import ObjectId


def build_page_condition(pipeline, page_number, page_size):
    if page_number is not None and page_size is not None:
        pipeline.append({"$skip": (page_number - 1) * page_size})
        pipeline.append({"$limit": page_size})
    return pipeline


# 获取所有有效的配置
def get_all_active_config(page_number=None, page_size=None):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    pipeline = [
        {
            '$match': {'is_delete': 0}
        },
        {
            '$sort': {'modify_time': -1}
        },
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
    ]
    build_page_condition(pipeline, page_number, page_size)
    # 执行聚合查询
    results = collection.aggregate(pipeline)
    return results


# 获取配置数量
def get_config_count():
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    return collection.count_documents({})


# 获取指定监控路径的配置
def get_active_by_monitor_path(add_monitor_path):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    return collection.find_one({'monitor_path': add_monitor_path, 'is_delete': 0})


# 获取指定监控路径的配置数量
def get_active_count_by_monitor_path(add_monitor_path):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    return collection.count_documents({'monitor_path': add_monitor_path, 'is_delete': 0})


# 获取指定ID获取的配置
def get_active_by_monitor_id(monitor_id):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    pipeline = [
        {'$match': {'is_delete': 0, '_id': ObjectId(monitor_id)}},
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
        }
    ]
    return collection.aggregate(pipeline)
    # return collection.find_one({'_id': ObjectId(monitor_id), 'is_delete': 0})


# 新增监控
def insert_config(config_info):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    result = collection.insert_one(config_info)
    return result.inserted_id


def update_config(condition, document):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    update = {'$set': {key: value for key, value in document.items()}}
    collection.update_one(condition, update)


# 删除监控(逻辑删除)
def del_config(condition):
    collection = MongoDBUtils.get_collection(config.MONGODB_SYNC_CONFIG_COLLECTION)
    collection.update_one(condition, {'$set': {'is_delete': 1}})
