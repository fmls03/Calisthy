import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueSessionStorage from 'vue-sessionstorage'
import '@mdi/font/css/materialdesignicons.css'
import Vuetify from 'vuetify/lib'

Vue.config.productionTip = false

Vue.use(VueSessionStorage);

new Vue({
  router,
  store,
  axios,
  vuetify,
  render: h => h(App)
}).$mount('#app')

export default new Vuetify({
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  },
})
