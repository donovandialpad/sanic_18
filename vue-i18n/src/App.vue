<template>
  <div id="app">
    <div v-if="isLoading">Loading...</div>
    <div v-else>
      <Nav />
      <div class="container">
      <div class="">
          <p>BABEL {{ message.message }}</p>
        </div>
      <router-view />
      </div>
      <Footer />
    </div>
  </div>
</template>


<script>
import Nav from "@/components/Nav.vue"
import Footer from "@/components/Footer.vue"
import EventBus from "@/EventBus"
import {
  setDocumentDirectionPerLocale,
  setDocumentLang,
  setDocumentTitle
} from "@/util/i18n/document"
import { loadLocaleMessagesAsync } from "@/i18n"
export default {
  components: { Nav, Footer },
  data() {
    return {
      message: 'Hello World!',
      isLoading: true
    }
  },
  methods: {
    getList() {
      this.axios.get('http://127.0.0.1:8000').then((response) => {
        this.message = response.data
      })
    }
  },
  created() {
    this.getList()
  },
  mounted() {
    EventBus.$on("i18n-load-start", () => (this.isLoading = true))
    EventBus.$on("i18n-load-complete", () => (this.isLoading = false))
  },
}
</script>


<style>
body {
  margin: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#app .container {
  padding: 1rem;
}
</style>