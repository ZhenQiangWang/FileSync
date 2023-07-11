<template>
  <div class="app-container">
    <el-table v-loading="loading" :data="logList">
      <el-table-column v-if="false" label="_ID" align="center" prop="monitor_id"/>
      <el-table-column label="操作类型" align="center" prop="event_type"/>
      <el-table-column label="文件名称" align="center" prop="file_name"/>
      <el-table-column label="监听路径" align="center" prop="src_path"/>
      <el-table-column label="目标路径" align="center" prop="tar_path"/>
      <el-table-column label="更新前文件名称" align="center" prop="rename_before_source_file_path"/>
      <el-table-column label="更新时间" align="center" prop="modify_time" width="180">
      </el-table-column>
    </el-table>
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.page_number"
      :limit.sync="queryParams.page_size"
      @pagination="getList"
    />
  </div>
</template>

<script>

import { get_sync_log_by_monitor_id } from '@/api/fileSync/syncLog'

export default {
  name: 'FileSyncLog',
  data() {
    return {
      // 遮罩层
      loading: true,
      // 总条数
      total: 0,
      // 表格数据
      logList: [],
      queryParams: {
        page_number: 1,
        page_size: 20,
        monitor_id: null
      }
    }
  },
  created() {
    const monitor_id = this.$route.params && this.$route.params.monitor_id
    if (monitor_id) {
      this.queryParams.monitor_id = monitor_id
      this.getList()
    }
  },
  methods: {
    getList() {
      this.loading = true
      get_sync_log_by_monitor_id(this.queryParams).then(response => {
        this.logList = response.data
        this.total = response.total
        this.loading = false
      })
    }
  }
}
</script>
