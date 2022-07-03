<template>
  <div>
    <div class="diagonal-box-top bg"></div>
    <!-- Top Toolbar -->
    <div>
      <div
        v-for="item in items"
        :key="item.name"
        text
        class="text-capitalize hidden-sm-and-down mx-1"
        :href="item.href"
        >
          <i class="mdi" :class="item.icon" />
          {{ item.name }}
        </div>
    </div>
  </div>
</template>

<script setup>
const drawer = ref(false);
const group = ref();
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
watch(group, () => {
  drawer.value = false;
})
</script>

<style scoped>
.diagonal-box-top {
  position: relative;
  padding-top: 192px;
  overflow: hidden;
  margin-top: -1px;
  margin-right: -16px;
}

.diagonal-box-top:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  transform: skewy(var(--angle));
  transform-origin: -5% 0;
}
</style>
