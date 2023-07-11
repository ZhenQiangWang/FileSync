<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="源路径" prop="monitor_path">
<!--        <el-input
          v-model="queryParams.monitor_path"
          placeholder="请输入同步源路径"
          clearable
        />-->

        <el-select
          v-model="queryParams.monitor_path"
          multiple
          filterable
          remote
          reserve-keyword
          placeholder="请输入同步源路径"
          :remote-method="remoteMethod"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>

      </el-form-item>

      <el-form-item label="目标路径" prop="target_path">
        <el-input
          v-model="queryParams.target_path"
          placeholder="请输入同步目标路径"
          clearable
        />
      </el-form-item>

      <el-form-item label="是否运行" prop="isRunning">
        <el-input
          v-model="queryParams.isRunning"
          placeholder="请选择"
          clearable
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
        <el-button type="success" icon="el-icon-folder-add" size="mini" @click="handleAdd">添加</el-button>
      </el-form-item>

    </el-form>

    <el-table v-loading="loading" :data="configList">
<!--      <el-table-column type="selection" width="55" align="center" />-->
      <el-table-column label="_ID" align="center" prop="_id" v-if="false" />
      <el-table-column label="监听路径" align="center" prop="monitor_path" />
      <el-table-column label="目标路径" align="center" prop="target_path" />
      <el-table-column label="同步规则" align="center" prop="rules" />
      <el-table-column label="是否包含子文件夹" align="center" width="150">
        <template slot-scope="scope">
          <el-switch
            disabled
            v-model="scope.row.recursive"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </template>
      </el-table-column>
      <el-table-column label="是否正在运行" align="center">
        <template slot-scope="scope">
          <el-switch
            disabled
            v-model="scope.row.is_running"
            :active-value = 1
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </template>
      </el-table-column>
      <el-table-column v-if="false" label="是否已删除" align="center" prop="is_delete" />
      <el-table-column label="创建时间" align="center" prop="modify_time" width="180">
      </el-table-column>
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-switch-button"
            @click="handleStart(scope.row)"
          >启动</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-video-pause"
            @click="handleStop(scope.row)"
          >暂停</el-button>

          <el-dropdown size="mini" @command="(command) => handleCommand(command, scope.row)">
            <el-button size="mini" type="text" icon="el-icon-d-arrow-right">更多</el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="handleSyncLog" icon="el-icon-link"
                                >同步日志</el-dropdown-item>
              <el-dropdown-item command="handleDel" icon="el-icon-delete"
                                >删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>

<!--          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleSyncLog(scope.row)"
          >同步日志</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
          >删除</el-button>-->

        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.page_number"
      :limit.sync="queryParams.page_size"
      @pagination="getList"
    />



<!--     添加或修改监控设置对话框 -->
    <el-dialog :title="title" :visible.sync="open" :close-on-click-modal = "false"	 width="600px" append-to-body>
      <el-form ref="form" :model="form" label-width="100px">
        <el-form-item label="ID" prop="Id">
          <el-input v-model="form._id" disabled="none" />
        </el-form-item>
        <el-form-item label="监听路径" prop="monitor_path">
          <el-input v-model="form.monitor_path" type="textarea" placeholder="请输入内容" />
        </el-form-item>
        <el-form-item label="目标路径" prop="target_path">
          <el-input v-model="form.target_path" type="textarea" placeholder="请输入内容" />
        </el-form-item>
        <el-form-item label="同步规则" prop="rules" >
          <el-tooltip  placement="right">
            <div slot="content">
              content="同步规则设置，规则如下：<br/>
              1、【file_path】为文件路径<br>
              2、基于python语法<br>
              3、同步时，符合该规则的文件则不同步<br>
              4、常用语法：{<br>
                4.1、获取路径：os.path.split(file_path)[0]<br>
                4.2、获取文件名：os.path.split(file_path)[1]<br>
                4.3、判断文件名中是否存在某个字符串：'A' in os.path.split(file_path)[1]<br>
                4.4、获取文件生成时间：os.path.getctime(file_path)<br>
                4.5、获取文件修改时间：os.path.getmtime(file_path)<br>
                4.6、判断文件生成时间是否在指定日期之前：os.path.getmtime(file_path) < time.mktime(time.strptime('2023-03-10 15:00:00', '%Y-%m-%d %H:%M:%S'))<br>
                4.7、判断文件名以'_'分割，第一位是否是指定字符串'A'：'A' == os.path.split(parent_path)[1].split('_')[0]<br>
                4.7、判断文件名以'_'分割，第一位是否包含指定字符串'A'：'A' in os.path.split(parent_path)[1].split('_')[0]<br>
              }<br>
              例：'A' in file_path  表示文件路径中存在'A'字符串的文件不同步
            </div>
            <i class="el-icon-question"></i>
          </el-tooltip>
          <el-input v-model="form.rules" type="textarea" placeholder="请输入内容" />
        </el-form-item>
        <el-form-item label="包含子文件夹" prop="recursive">
          <template>
            <el-switch
              v-model="form.recursive"
              active-color="#13ce66"
              inactive-color="#ff4949"
            ></el-switch>
          </template>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>

import {
  listConfig,
  getConfig,
  updateConfig,
  addConfig,
  delConfig,
  startMonitor,
  stopMonitor
} from '@/api/fileSync/syncConfig'


export default {
  name: 'FileSync',
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 表格数据
      configList: [],
      // 弹出层标题
      title: "同步设置更新",
      // 是否显示弹出层
      open: false,
      // 查询参数
      queryParams: {
        page_number: 1,
        page_size: 10,
        monitorPath: null,
        targetPath: null,
        isRunning: null,
      },
      options:[],
      value: [],
      list: [],
      states:[],
      // 表单参数
      form: {},
      // 表单校验
      rules: {}
    };
  },
  created() {
    this.getList()
  },
  mounted() {
    this.list = this.states.map(item => {
      return { value: `value:${item}`, label: `label:${item}` };
    });
  },
  methods: {
    /** 查询监控设置列表 */
    getList() {
      this.loading = true
      listConfig(this.queryParams).then(response => {
        this.configList = response.data
        this.total = response.total
        this.loading = false
      });
    },
    // 取消按钮
    cancel() {
      this.open = false
      this.reset()
    },
    // 表单重置
    reset() {
      this.form = {}
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.queryParams.pageNum = 1
      this.getList()
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm")
      this.handleQuery();
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.Id)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset()
      // this.form.recursive = false
      // this.form.rules = ""
      this.open = true
      this.title = "添加监控设置"
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      const monitor_id = row._id
      getConfig(monitor_id).then(response => {
        this.form = response.data
        this.open = true
        this.title = "修改配置"
      });
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          if(this.form.recursive === undefined){
            this.form.recursive = false
          }

          if(this.form.rules === undefined){
            this.form.rules = ""
          }

          if (this.form._id !== undefined && this.form._id != null) {
            updateConfig(this.form).then(response => {
              {
                this.$message({
                  message: '修改成功',
                  type: 'success'
                });
              }
              this.open = false;
              this.getList();
            });
          } else {
            addConfig(this.form).then(response => {
              {
                this.$message({
                  message: '新增成功',
                  type: 'success'
                });
              }
              this.open = false;
              this.getList();
            });
          }
        }
      });
    },

    handleStart(row){
      const id = row._id
      startMonitor(id).then(response => {
        {
          this.$message({message: '启动成功', type: 'success' });
        }
        this.getList();
      });
    },
    handleStop(row){
      const id = row._id
      stopMonitor(id).then(response => {
        {
          this.$message({message: '暂停成功', type: 'success' });
        }
        this.getList();
      });
    },
    /** 删除按钮操作 */
    handleDelete(row) {
      const id = row._id
      this.$confirm('是否确认删除监听路径为："' + row.monitor_path + '"的数据项？').then(function() {
        return delConfig(id)
      }).then(() => {
        this.getList()
        this.$message({ message: '删除成功',type: 'success' });
      }).catch(() => {});
    },

    // 同步日志
    handleSyncLog(row){
      const monitor_id = row._id
      this.$router.push("/fileSync/fileSyncLog/"+monitor_id);
    },
    remoteMethod(query) {
      if (query !== '') {
        // this.loading = true;
        setTimeout(() => {
          // this.loading = false;
          this.options = this.list.filter(item => {
            return item.label.toLowerCase()
              .indexOf(query.toLowerCase()) > -1;
          });
        }, 200);
      } else {
        this.options = [];
      }
    },
    // 更多操作触发
    handleCommand(command, row) {
      switch (command) {
        case "handleSyncLog":
          this.handleSyncLog(row);
          break;
        case "handleDel":
          this.handleDelete(row);
          break;
        default:
          break;
      }
    },

  },

}
</script>
