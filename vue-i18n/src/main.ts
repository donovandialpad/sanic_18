import Vue from 'vue'
import axios from 'axios'
import i18n from "./i18n";
import VueAxios from 'vue-axios'
import router from "./router";
import VueCompositionAPI, { createApp, h } from '@vue/composition-api'

import App from './App.vue'

Vue.use(VueAxios, axios)
Vue.use(VueCompositionAPI)
Vue.config.productionTip = false;

const app = createApp({
  i18n,
  router,
  render: () => h(App)
})

app.mount('#app')
