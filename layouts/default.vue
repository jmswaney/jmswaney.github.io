<template>
  <!-- App bar -->
  <VAppBar class="app-bar-color">
    <div class="flex grow justify-end mx-8">
      <template v-for="appBarBtn in appBarBtns" :key="appBarBtn.label">  
        <VBtn variant="text" :to="appBarBtn.to">
          {{ appBarBtn.label }}
        </VBtn>
      </template>
    </div>
  </VAppBar>
  <!-- Main content -->
  <VMain class="mt-4 mx-32">
    <slot />
  </VMain>
  <!-- Footer -->
  <VFooter class="flex flex-col gap-2">
    <div class="flex">
      <VBtn
        v-for="(socialBtn, idx) in socialBtns"
        :key="idx"
        :icon="socialBtn.icon"
        variant="text"
        size="small"
        target="_blank"
        rel="noopener noreferrer"
      />
    </div>
    <div>
      &copy; {{ new Date().getFullYear() }}
    </div>
  </VFooter>
</template>

<script setup>
const appBarBtns = [
  { label: "About", to: "/" },
  { label: "Profile", to: "/profile" },
  { label: "Projects", to: "/projects" },
  { label: "Blog", to: "https://blog.jmswaney.com" }
]

const socialBtns = [
  { icon: 'mdi-twitter', href: 'https://twitter.com/justinmswaney' },
  { icon: 'mdi-linkedin', href: 'https://www.linkedin.com/in/jmswaney/' },
  { icon: 'mdi-instagram', href: 'https://www.instagram.com/jswaymusic' },
  { icon: 'mdi-github-circle', href: 'https://github.com/jmswaney' },
]
</script>

<style scoped>
.app-bar-color {
  @apply bg-indigo-600
}
</style>
