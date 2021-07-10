<template>
  <v-container justify="center">
    <HomeAvatar />
    <v-card flat class="pa-2 mx-auto" max-width="500px" color="grey lighten-4">
      <nuxt-content :document="about" />
    </v-card>
  </v-container>
</template>

<script>
import HomeAvatar from '@/components/HomeAvatar'

export default {
  components: { HomeAvatar },
  async asyncData({ $content }) {
    const about = await $content('about').fetch()
    return { about }
  },
}
</script>
