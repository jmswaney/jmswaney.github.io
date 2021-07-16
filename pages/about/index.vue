<template>
  <v-container justify="center">
    <HomeAvatar />
    <v-card flat class="pa-2 mx-auto" max-width="500px" color="grey lighten-4">
      <nuxt-content :document="about" />
    </v-card>
  </v-container>
</template>

<script lang="ts">
import HomeAvatar from './HomeAvatar.vue'
import useContent from '~/composition/useContent'

interface About {
  title: string
  description: string
}

export default {
  components: { HomeAvatar },
  setup() {
    const { data: about } = useContent<About>('about')
    return { about }
  }
}
</script>
