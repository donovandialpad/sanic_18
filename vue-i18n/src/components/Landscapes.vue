<template>
  <div class="landscapes">
    <Landscape v-bind="landscape" v-for="landscape in landscapes" :key="landscape.id" />
  </div>
</template>
<script>
import Landscape from "./Landscape.vue"
export default {
  data: () => ({
    landscapes: []
  }),
  created() {
    this.axios.get('http://127.0.0.1:8000/get_data').then((response) => {
        this.landscapes = response.data
      })
  },
  components: { Landscape }
}
</script>
<style scoped>
.landscapes {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
</style>