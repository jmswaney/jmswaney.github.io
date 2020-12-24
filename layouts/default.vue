<template>
  <v-app>
    <AppBarWithNav />
    <!-- Main Content -->
    <v-main class="grey lighten-4">
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
  --angle: -3deg;
  --indigo: #3f51b5;
}

.bg:before {
  background-color: #3f51b5;
}
</style>
