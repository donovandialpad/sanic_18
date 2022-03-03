<template>
  <div class="home">
   <h1 v-t="'app.title'" />
    <Landscapes />
  </div>
</template>
<script>
import Landscapes from "@/components/Landscapes.vue"
export default {
  name: "home",
  components: {
    Landscapes
  }
}
</script>