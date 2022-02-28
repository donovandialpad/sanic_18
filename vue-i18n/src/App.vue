<script>
export default {
  data() {
    return {
      message: 'Hello World!',
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
  <div class="">
    <p>i18n {{ $t('message.hello') }}</p>
    <p>BABEL {{ message.message }}</p>
  </div>
</template>

