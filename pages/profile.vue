<template>
  <v-row justify="center">
    <v-col cols="auto">
      <v-card
        flat
        max-width="500"
        color="grey lighten-4"
        style="margin-top: -32px"
      >
        <v-card-title>
          <span class="tw-font-light tw-text-2xl">{{ profile.title }}</span>
        </v-card-title>
        <v-card-subtitle>{{ profile.description }}</v-card-subtitle>
        <v-card-text>
          <!-- Education -->
          <h1 class="tw-pb-3 tw-text-xl tw-font-light">Education</h1>
          <h1 class="tw-font-normal">
            {{ profile.education.graduate.level }} in
            {{ profile.education.graduate.field }}
          </h1>
          <h1 class="tw-pb-3 tw-font-medium">
            {{ profile.education.graduate.school }},
            {{ profile.education.graduate.year }}
          </h1>
          <h1 class="tw-font-normal">
            {{ profile.education.undergraduate.level }} in
            {{ profile.education.undergraduate.field }}
          </h1>
          <h1 class="tw-pb-4 tw-font-medium">
            {{ profile.education.undergraduate.school }},
            {{ profile.education.undergraduate.year }}
          </h1>
          <!-- Experience -->
          <h1 class="tw-pb-3 tw-text-xl tw-font-light">Experience</h1>
          <h1>{{ profile.experience.samply.role }}</h1>
          <h1>{{ profile.experience.samply.company }}</h1>
          <h1 class="tw-pb-3">
            {{ profile.experience.samply.start }} -
            {{ profile.experience.samply.end || 'Present' }}
          </h1>
          <h1>{{ profile.experience.fulcrum.role }}</h1>
          <h1>{{ profile.experience.fulcrum.company }}</h1>
          <h1 class="tw-pb-3">
            {{ profile.experience.fulcrum.start }} -
            {{ profile.experience.fulcrum.end || 'Present' }}
          </h1>
          <!-- Publications -->
          <!-- <h1 class="tw-pb-3 tw-text-lg tw-font-light">Publications</h1>
          <ul
            v-for="publication of profile.publications"
            :key="publication.name"
            class="px-0 pb-2"
          >
            <li>
              <span class="tw-text-sm">
                {{ publication.title }}
              </span>
            </li>
          </ul> -->
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'
import { useContent } from '@/composition/useProject'

export default defineComponent({
  setup() {
    return { profile: useContent('profile') }
  },
})
</script>
