<template>
  <v-app>
    <AppBarWithNav />
    <!-- Main Content -->
    <v-main>
      <Nuxt />
    </v-main>
    <AppFooter />
  </v-app>
</template>

<script>
import AppBarWithNav from '@/components/AppBarWithNav'
import AppFooter from '@/components/AppFooter'

export default {
  components: { AppBarWithNav, AppFooter },
}
</script>

<style>
:root {
  --angle: -4deg;
}

.bg:before {
  background-color: #3f51b5;
}
</style>
