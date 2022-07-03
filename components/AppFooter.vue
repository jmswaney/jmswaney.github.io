<template>
  <div>
    <footer>
      <div
        flat
        tile
        light
        width="100%"
        class="text-center"
      >
          <div
            v-for="(socialBtn, idx) in socialBtns"
            :key="idx"
            icon
            :href="socialBtn.href"
            target="_blank"
            rel="noopener noreferrer"
            class="mx-2 button-hover"
          >
            <!-- <v-icon size="24px">{{ socialBtn.icon }}</v-icon> -->
            
            <i class="mdi"  :class="socialBtn.icon" />
          </div>
          &copy; {{ new Date().getFullYear() }}
      </div>
    </footer>
  </div>
</template>

<script setup>
const socialBtns = [
  { icon: 'mdi-twitter', href: 'https://twitter.com/justinmswaney' },
  { icon: 'mdi-linkedin', href: 'https://www.linkedin.com/in/jmswaney/' },
  { icon: 'mdi-instagram', href: 'https://www.instagram.com/jswaymusic' },
  { icon: 'mdi-github-circle', href: 'https://github.com/jmswaney' },
]
</script>

<style scoped>
.diagonal-box-btm {
  position: relative;
  padding-bottom: 128px;
  overflow: hidden;
  margin-top: -1px;
  margin-right: -16px;
}

.diagonal-box-btm:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  transform: skewy(var(--angle));
  transform-origin: 105% 0;
  padding-bottom: 256px;
}

.button-hover:hover {
  color: var(--indigo);
}
</style>
