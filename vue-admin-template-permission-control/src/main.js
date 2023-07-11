import Vue from 'vue'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en' // lang i18n

// import '@/styles/index.scss' // global css


import './assets/styles/element-variables.scss'

import '@/assets/styles/index.scss' // global css
import '@/assets/styles/ruoyi.scss' // ruoyi css

import App from './App'
import store from './store'
import plugins from './plugins' // plugins
import router from './router'
// 头部标签组件
import VueMeta from 'vue-meta'

import '@/icons' // icon
import '@/permission' // permission control
// 分页组件
import Pagination from "@/components/Pagination";


/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
if (process.env.NODE_ENV === 'production') {
  const { mockXHR } = require('../mock')
  mockXHR()
}
// 全局组件挂载
Vue.config.productionTip = false


// set ElementUI lang to EN
Vue.use(ElementUI, { locale })
// 如果想要中文版 element-ui，按如下方式声明
// Vue.use(ElementUI)
Vue.use(VueMeta)
Vue.use(plugins)
// Vue.use(directive)
Vue.component('Pagination', Pagination)

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
