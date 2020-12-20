<template>
  <v-app>
    <!-- Top Toolbar -->
    <v-toolbar color="indigo" flat dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-toolbar>
    <div class="diagonal-box-top bg"></div>
    <!-- Nav Drawer -->
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="indigo--text">
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <!-- Main Content -->
    <v-main>
      <Nuxt />
    </v-main>
    <!-- Footer -->
    <div class="diagonal-box-btm bg"></div>
    <v-footer dark padless color="indigo">
      <v-card flat tile width="100%" color="indigo white--text text-center">
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
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      group: null,
      socialBtns: [
        { icon: 'mdi-twitter', href: 'https://twitter.com/justinmswaney' },
        { icon: 'mdi-linkedin', href: 'https://www.linkedin.com/in/jmswaney/' },
        { icon: 'mdi-instagram', href: 'https://www.instagram.com/jswaymusic' },
        { icon: 'mdi-github', href: 'https://github.com/jmswaney' },
      ],
    }
  },
  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>

<style>
:root {
  --angle: -4deg;
}

.diagonal-box-top {
  position: relative;
  padding: 64px 0;
  margin-top: -1px;
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

.diagonal-box-btm {
  position: relative;
  padding: 64px 0;
  margin-top: -1px;
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
  outline: 1px solid transparent;
  backface-visibility: hidden;
}

.bg:before {
  background-color: #3f51b5;
}
</style>
