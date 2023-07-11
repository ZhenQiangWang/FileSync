# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 文件同步实现

import os.path
import shutil
from datetime import  datetime
from core.file_sync.FileSyncEventType import FileSyncEventType
from core.file_sync.Repository.SyncLogRepository import *
from common.LogUtils import LogUtils


# 获取日志记录器
log = LogUtils.log


def log_save(monitor_id, event_type, src_path, tar_path, file_name, rename_before_source_file_path):
    # 构建日志文档
    log_doc = {
        'monitor_id': monitor_id,
        'event_type': event_type,
        'file_name': file_name,
        'src_path': src_path,
        'tar_path': tar_path,
        'rename_before_source_file_path': rename_before_source_file_path,
        'modify_time': datetime.now()
    }
    save_sync_log(log_doc)


def sync(monitor_id, src_path, tar_path, event_type, rename_before_source_file_path=None):
    if event_type == FileSyncEventType.RENAME:
        # 重命名，文件名需同步修改
        log.info("ID:%s,RENAME------%s %s %s", monitor_id, src_path, tar_path, rename_before_source_file_path)
        shutil.copy2(src_path, tar_path, follow_symlinks=True)
        if os.path.exists(rename_before_source_file_path):
            os.remove(rename_before_source_file_path)
    elif event_type == FileSyncEventType.MODIFY:
        # 文件新增、修改，需同步更新
        log.info("ID:%s,MODIFY------%s %s", monitor_id, src_path, tar_path)
        shutil.copy2(src_path, tar_path, follow_symlinks=True)
    elif event_type == FileSyncEventType.DELETE:
        # 文件删除，需同步删除
        log.info("ID:%s,DELETE------%s %s", monitor_id, src_path, tar_path)
        if os.path.exists(tar_path):
            os.remove(tar_path)

    # 记录日志到MongoDB
    log_save(monitor_id, event_type.name, src_path, tar_path, os.path.basename(src_path), rename_before_source_file_path)
