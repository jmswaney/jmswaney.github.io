<template>
  <v-card flat max-width="360" class="mx-2 transparent">
    <v-img width="100%" :src="project.image" class="mx-auto"> </v-img>
    <v-card-title class="headline pb-0">
      {{ project.title }}
    </v-card-title>
    <v-card-text class="tw-prose">
      <nuxt-content :document="project"></nuxt-content>
      <template v-for="link of project.links">
        <v-icon :key="`icon-${link.name}`">{{ link.icon }}</v-icon>
        <a :key="link.name" :href="link.href">
          {{ link.name }}
        </a>
        <br :key="`br-${link.name}`" />
      </template>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
import { useProject } from '@/composition/Projects'

export default defineComponent({
  props: {
    path: {
      type: String,
      default: '',
    },
  },
  setup(props) {
    return { ...useProject(props.path) }
  },
})
</script>
