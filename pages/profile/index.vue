<template>
  <v-row justify="center">
    <v-col cols="auto">
      <v-card
        flat
        max-width="500"
        color="grey lighten-4"
        style="margin-top: -32px"
      >
        <v-card-title class="text-h5 font-weight-light">
          {{ profile.title }}
        </v-card-title>
        <v-card-subtitle class="text-body-1">{{
          profile.description
        }}</v-card-subtitle>
        <v-card-text>
          <!-- Education -->
          <h1 class="pb-3 text-h6 font-weight-light">Education</h1>
          <education-entry
            v-for="entry in profile.education"
            :key="entry.level"
            :entry="entry"
          />
          <!-- Experience -->
          <h1 class="pb-3 text-h6 font-weight-light">Experience</h1>
          <experience-entry
            v-for="entry in profile.experience"
            :key="entry.company"
            :entry="entry"
          />
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
import { useContent } from '@/composition/useProject'
import EducationEntry from './EducationEntry.vue'
import ExperienceEntry from './ExperienceEntry.vue'

export default defineComponent({
  components: { EducationEntry, ExperienceEntry },
  setup() {
    return { profile: useContent('profile') }
  },
})
</script>
