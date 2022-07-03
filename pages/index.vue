<template>
  <v-container justify="center">
    <HomeAvatar />
    <v-card flat class="pa-2 mx-auto" max-width="500px">
      <ContentDoc />
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
interface About {
  title: string
  description: string
}

// const { page: about } = useContent()
</script>
