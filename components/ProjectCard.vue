<template>
  <div v-if="project">
    <img
      v-if="project.image !== undefined"
      :src="project.image.src"
      alt="project-img"
    >
    <h2 class="headline pb-0">
      {{ project.title }}
    </h2>
    <!-- <nuxt-content :document="project"></nuxt-content> -->
    <template v-for="link of project.links" :key="link.name">
      <i class="mdi" :class="link.icon" />
      <a :href="link.href" target="_blank">
        {{ link.name }}
      </a>
      <br />
    </template>
  </div>
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
