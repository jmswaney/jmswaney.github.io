<template>
  <div>
    <footer class="">
      <div
        v-for="(socialBtn, idx) in socialBtns"
        :key="idx"
        target="_blank"
        rel="noopener noreferrer"
      >        
        <i class="mdi" :class="socialBtn.icon" />
      </div>
      <p>
        &copy; {{ new Date().getFullYear() }}
      </p>
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
