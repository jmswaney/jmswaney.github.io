<template>
  <v-card flat max-width="360" class="mx-2 transparent">
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
      <nuxt-content :document="project"></nuxt-content>
      <template v-for="link of project.links">
        <v-icon :key="`icon-${link.name}`">{{ link.icon }}</v-icon>
        <a :key="link.name" :href="link.href" target="_blank">
          {{ link.name }}
        </a>
        <br :key="`br-${link.name}`" />
      </template>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
import useContent from '~/composition/useContent'

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

export default defineComponent({
  props: {
    path: { type: String, required: true },
  },
  setup(props) {
    const { data: project } = useContent<Project>(props.path)
    return { project }
  },
})
</script>
