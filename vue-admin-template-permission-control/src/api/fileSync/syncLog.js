import request from '@/utils/request'

// 查询定时任务调度列表
export function get_sync_log_by_monitor_id(query) {
  return request({
    url: '/fileSync/get_sync_log_by_monitor_id',
    method: 'post',
    data: query
  })
}
