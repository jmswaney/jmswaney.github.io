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
          <div v-for="entry in profile.education">
            <h1 class="text-body-2">{{ entry.level }} in {{ entry.field }}</h1>
            <h1 class="pb-3 text-body-2 font-weight-medium">
              {{ entry.school }}, {{ entry.year }}
            </h1>
          </div>
          <!-- Experience -->
          <h1 class="pb-3 text-h6 font-weight-light">Experience</h1>
          <div v-for="entry in profile.experience">
            <h1 class="text-body-2">{{ entry.role }}</h1>
            <h1 class="text-body-2 font-weight-medium">
              {{ entry.company }}
            </h1>
            <h1 class="pb-3 text-body-2">{{ entry.start }} - {{ entry.end || 'Present' }}</h1>
          </div>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent, Ref } from '@nuxtjs/composition-api'
import useContent from '~/composition/useContent'

interface Education {
  level: string
  field: string
  school: string
  year: number
}

interface Experience {
  role: string
  company: string
  start: number
  end?: number
}

interface Profile {
  title: string
  description: string
  education: {
    undergraduate: Education
    graduate: Education
  }
  experience: {
    fulcrum: Experience
    samply: Experience
  }
}

export default defineComponent({
  setup() {
    const { data: profile } = useContent<Profile>('profile')
    return { profile }
  },
})
</script>
