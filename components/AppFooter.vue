<template>
  <div>
    <!-- Footer -->
    <div class="diagonal-box-btm bg"></div>
    <v-footer dark padless>
      <v-card
        flat
        tile
        width="100%"
        color="indigo"
        class="white--text text-center"
      >
        <v-card-text>
          <v-btn
            v-for="(socialBtn, idx) in socialBtns"
            :key="idx"
            icon
            :href="socialBtn.href"
            target="_blank"
            rel="noopener noreferrer"
            class="mx-2 white--text"
          >
            <v-icon size="24px">{{ socialBtn.icon }}</v-icon>
          </v-btn>
        </v-card-text>
        <v-card-text> &copy; {{ new Date().getFullYear() }} </v-card-text>
      </v-card>
    </v-footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      socialBtns: [
        { icon: 'mdi-twitter', href: 'https://twitter.com/justinmswaney' },
        { icon: 'mdi-linkedin', href: 'https://www.linkedin.com/in/jmswaney/' },
        { icon: 'mdi-instagram', href: 'https://www.instagram.com/jswaymusic' },
        { icon: 'mdi-github', href: 'https://github.com/jmswaney' },
      ],
    }
  },
}
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
</style>
