import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueI18n from 'vue-i18n'
const app = createApp(App)
const messages = {
    en: {
      message: {
        hello: 'hello world'
      }
    },
    ja: {
      message: {
        hello: 'こんにちは、世界'
      }
    }
  }
  
  // Create VueI18n instance with options
  const i18n = new VueI18n({
    locale: 'ja', // set locale
    messages, // set locale messages
  })


app.use(VueAxios, axios)
app.use(router)
app({ i18n }).mount('#app')