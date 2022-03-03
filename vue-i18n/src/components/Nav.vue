<template>
  <div class="nav">
    <div class="nav__start">
      <LocalizedLink to="/">{{ $t("nav.home") }}</LocalizedLink>
      <LocalizedLink to="/about">{{ $t("nav.about") }}</LocalizedLink>
    </div>
    <div class="nav__end">
      <p class="user-greeting">{{ $t("app.user_greeting", { name: "Donovan" }) }}</p>
      <LocaleSwitcher />
    </div>
  </div>
</template>
<script>
import LocaleSwitcher from "@/components/LocaleSwitcher.vue"
import LocalizedLink from "@/components/LocalizedLink.vue"
export default {
  components: { LocaleSwitcher, LocalizedLink}
}
</script>
<style scoped>
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  padding: 1rem;
  color: #fff;
  background-color: #3d536a;
}
.nav__start,
.nav__end {
  display: flex;
  align-items: center;
}
.nav img {
  margin-right: 1rem;
}
.nav a {
  margin-right: 1.5rem;
  font-weight: bold;
  color: #fff;
  text-decoration: none;
}
</style>