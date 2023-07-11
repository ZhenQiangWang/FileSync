import request from '@/utils/request'

// 查询定时任务调度列表
export function listConfig(data) {
  return request({
    url: '/fileSync/get_all_monitor',
    method: 'post',
    data: data
  })
}

export function getConfig(monitor_id) {
  return request({
    url: '/fileSync/get_monitor_by_id',
    method: 'get',
    params: { monitor_id }
  })
}

export function updateConfig(form){
  return request({
    url: '/fileSync/update_monitor',
    method: 'post',
    data: form
  })
}

export function addConfig(form){
  return request({
    url: '/fileSync/add_monitor',
    method: 'post',
    data: form
  })
}

export function delConfig(monitor_id){
  return request({
    url: '/fileSync/remove_monitor',
    method: 'get',
    params: { monitor_id }
  })
}


export function startMonitor(monitor_id){
  return request({
    url: '/fileSync/start_monitor',
    method: 'get',
    params: { monitor_id }
  })
}

export function stopMonitor(monitor_id){
  return request({
    url: '/fileSync/stop_monitor',
    method: 'get',
    params: { monitor_id }
  })
}
