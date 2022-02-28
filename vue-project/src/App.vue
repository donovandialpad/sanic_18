<script>
export default {
  data() {
    return {
      message: 'Hello World!',
      name: 'HelloI18n'
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
  }
}
</script>

<template>
  <h1>{{ message.message }}</h1>
</template>

