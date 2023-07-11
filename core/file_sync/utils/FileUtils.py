# @Author   :zhenqiang.wang
# @Time     :2023/6/14 15:03
# 文件处理工具类

import os


# 组成新路径
def build_target_path(file_path, source_path, target_path):
    split = os.path.split(file_path)
    return os.path.join(target_path, split[1])
