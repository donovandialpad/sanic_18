<template>
  <div class="landscape">
    <h3>{{ title }}</h3>
    <img :src="imgUrl" />
    <div class="landscape__footer">
      <p>
        {{ $t("landscape.added") }}
        {{ $d(new Date(addedOn), "short") }}
      </p>
      <p>{{$tc("landscape.likes", likes)}}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    title: String,
    imgUrl: String,
    addedOn: String,
    likes: Number
  }
}
</script>
<style scoped>
.landscape {
  width: 30%;
  margin-bottom: 2rem;
  border: 1px solid #f2f2f2;
  border-radius: 4px;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}
h3 {
  margin: 0;
  padding: 0.5em;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
img {
  width: 100%;
}
p {
  text-align: center;
  margin: 0;
  padding: 0.5em;
}
</style>