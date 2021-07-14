import Vue from 'vue'
import '@mdi/font/css/materialdesignicons.css'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import axios from 'axios' //追記
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
import VueAxiosPlugin from "./plugins/vue-axios";
// import VueAxios from 'vue-axios' //追記
// import VueSwal from 'vue-swal'
// Vue.use(VueSwal)

Vue.use(VueAxiosPlugin, { axios: axios })
Vue.use(VueSweetalert2);
Vue.config.productionTip = false

// Vue.use(VueAxios, axios) //追記

new Vue({
  vuetify,
  router,
  icons: {
    iconfont: 'mdi', // 追加
  },
  render: h => h(App)
}).$mount('#app')