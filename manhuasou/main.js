import Vue from 'vue'
import App from './App'
//引入vuex
import store from './store'
//把vuex定义成全局组件
Vue.prototype.$store = store
Vue.config.productionTip = false
Vue.prototype.weburl = 'http://192.168.2.100';  


App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()




 



