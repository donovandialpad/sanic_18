import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueI18n from 'vue-i18n'
import VueCompositionAPI, { createApp, h } from '@vue/composition-api'

import App from './App.vue'

Vue.use(VueI18n)
Vue.use(VueAxios, axios)
Vue.use(VueI18n)
Vue.use(VueCompositionAPI)

const i18n = new VueI18n({
  locale: 'ja',
  messages: {
      en: {
          message: {
              hello: 'hello world'
          },
      },
      ja: {
          message: {
              hello: 'こんにちは、世界'
          }
      }
  }
});
Vue.config.productionTip = false;

const app = createApp({
  i18n,
  render: () => h(App)
})

app.mount('#app')
