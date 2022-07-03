<template>
  <v-card v-if="project" flat max-width="360" class="mx-2 transparent">
    <v-img
      v-if="project.image !== undefined"
      width="100%"
      max-height="200"
      :src="project.image.src"
      :lazy-src="project.image.lazySrc || ''"
      class="mx-auto"
    >
    </v-img>
    <v-card-title class="headline pb-0">
      {{ project.title }}
    </v-card-title>
    <v-card-text class="">
      <!-- <nuxt-content :document="project"></nuxt-content> -->
      <template v-for="link of project.links" :key="link.name">
        <v-icon >{{ link.icon }}</v-icon>
        <a :href="link.href" target="_blank">
          {{ link.name }}
        </a>
        <br />
      </template>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
interface Link {
  name: string
  icon: string
  href: string
}

interface Project {
  title: string
  description: string
  image: {
    src: string
    lazySrc: string
  }
  links: Link[]
}

const props = defineProps({
  path: { type: String, required: true }
})

const { page: project } = useContent()
</script>
