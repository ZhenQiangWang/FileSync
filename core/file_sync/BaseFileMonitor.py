# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 文件监控基类

from core.file_sync.FileSyncEventType import FileSyncEventType
import core.file_sync.SyncFile as sync_file
from watchdog.events import FileSystemEventHandler
from core.file_sync.utils import CheckRulesUtil
from core.file_sync.utils import FileUtils
from common.LogUtils import LogUtils
from core.file_sync.utils.CheckRulesUtil import check_rules

log = LogUtils.getLog()


class BaseFileMonitor(FileSystemEventHandler):

    def __init__(self, source_path, target_path, rules, monitor_id=None):
        self.monitor_id = monitor_id
        self.source_path = source_path
        self.target_path = target_path
        self.rules = rules

    def on_modified(self, event):
        try:
            if not event.is_directory:
                file_source_path = event.src_path
                if CheckRulesUtil.is_rel_file(file_source_path):
                    if check_rules(self.monitor_id, self.rules, file_source_path):
                        target_path = FileUtils.build_target_path(file_source_path, self.source_path, self.target_path)
                        sync_file.sync(self.monitor_id, file_source_path, target_path, FileSyncEventType.MODIFY)
                    else:
                        sync_file.log_save(self.monitor_id, FileSyncEventType.IGNORE.name, file_source_path, "", "", "")
        except Exception as ex:
            log.exception(ex)

    def on_deleted(self, event):
        try:
            if not event.is_directory:
                file_source_path = event.src_path
                if CheckRulesUtil.is_rel_file(file_source_path):
                    target_path = FileUtils.build_target_path(file_source_path, self.source_path, self.target_path)
                    sync_file.sync(self.monitor_id, file_source_path, target_path, FileSyncEventType.DELETE)
        except Exception as ex:
            log.exception(ex)

    def on_moved(self, event):
        try:
            if not event.is_directory:
                file_source_path = event.src_path
                dest_path = event.dest_path
                if CheckRulesUtil.is_rel_file(file_source_path) and CheckRulesUtil.is_rel_file(dest_path):
                    if check_rules(self.monitor_id, self.rules, file_source_path):
                        target_path = FileUtils.build_target_path(dest_path, self.source_path, self.target_path)
                        rename_before_source_file_path = FileUtils.build_target_path(file_source_path, self.source_path,
                                                                                     self.target_path)
                        sync_file.sync(self.monitor_id, dest_path, target_path, FileSyncEventType.RENAME,
                                       rename_before_source_file_path)
                    else:
                        sync_file.log_save(self.monitor_id, FileSyncEventType.IGNORE.name, file_source_path, "", "", "")
        except Exception as ex:
            log.exception(ex)
