import tab from './tab'
import cache from './cache'

export default {
  install(Vue) {
    // 页签操作
    Vue.prototype.$tab = tab
    // 缓存对象
    Vue.prototype.$cache = cache
  }
}
