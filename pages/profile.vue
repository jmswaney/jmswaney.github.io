<template>
  <div
    v-if="profile"
    flat
    max-width="500"
    style="margin-top: -32px"
  >
    <h1>
      {{ profile.title }}
    </h1>
    <p>
      {{ profile.description }}
    </p>
    <!-- Education -->
    <h1 class="pb-3 text-h6 font-weight-light">Education</h1>
    <div v-for="entry in profile.education" :key="entry.school">
      <h1 class="text-body-2">{{ entry.level }} in {{ entry.field }}</h1>
      <h1 class="pb-3 text-body-2 font-weight-medium">
        {{ entry.school }}, {{ entry.year }}
      </h1>
    </div>
    <!-- Experience -->
    <h1 class="pb-3 text-h6 font-weight-light">Experience</h1>
    <div v-for="entry in profile.experience" :key="entry.company">
      <h1 class="text-body-2">{{ entry.role }}</h1>
      <h1 class="text-body-2 font-weight-medium">
        {{ entry.company }}
      </h1>
      <h1 class="pb-3 text-body-2">
        {{ entry.start }} - {{ entry.end || 'Present' }}
      </h1>
    </div>
  </div>
</template>

<script setup lang="ts">
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

const { page: profile } = useContent();
</script>
