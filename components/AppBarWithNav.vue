<template>
  <div class="pb-48 pt-2 diagonal-box-top">
    <div class="flex justify-end mx-2">
      <div
        v-for="item in items"
        :key="item.name"
        class="basis-20 flex justify-center font-semibold text-sm text-slate-100 py-1 rounded-md hover:bg-indigo-700"
      >
        <NuxtLink :to="item.href">
          {{ item.name }}
        </NuxtLink>
      </div>
    </div>
    
  </div>
</template>

<script setup>
const items = [
  {
    name: 'About',
    icon: 'mdi-home',
    href: '/',
  },
  {
    name: 'Profile',
    icon: 'mdi-account',
    href: '/profile',
  },
  {
    name: 'Projects',
    icon: 'mdi-folder',
    href: '/projects',
  },
  {
    name: 'Blog',
    icon: 'mdi-post',
    href: 'https://blog.jmswaney.com',
  },
]
</script>

<style scoped>
.diagonal-box-top {
  position: relative;
}

.diagonal-box-top:before {
  @apply bg-indigo-600;
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  transform: skewy(-4deg);
  transform-origin: -5% 0;
  z-index: -1;
}
</style>
