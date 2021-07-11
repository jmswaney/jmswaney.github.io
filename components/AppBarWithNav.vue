<template>
  <div class="grey lighten-4">
    <div class="diagonal-box-top bg"></div>
    <!-- Top Toolbar -->
    <v-app-bar color="indigo" flat dark app dense scroll-threshold="128">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn
        v-for="item in items"
        :key="item.name"
        text
        class="text-capitalize hidden-sm-and-down mx-1"
        :href="item.href"
        >{{ item.name }}</v-btn
      >
    </v-app-bar>
    <!-- Nav Drawer -->
    <v-navigation-drawer v-model="drawer" temporary app color="grey lighten-4">
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="indigo--text">
          <v-list-item v-for="item in items" :key="item.name" :href="item.href">
            <v-icon left>{{ item.icon }}</v-icon>
            <v-list-item-title>{{ item.name }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      group: null,
      items: [
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
