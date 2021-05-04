<template>
  <v-row justify="center" style="margin-top: -192px" class="py-0">
    <v-col cols="auto">
      <project-card path="projects/scout" />
    </v-col>
    <v-col cols="auto">
      <project-card path="projects/sample-manager" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
import ProjectCard from '@/components/ProjectCard.vue'

export default defineComponent({
  components: { ProjectCard },
})
</script>
