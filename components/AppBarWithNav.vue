<template>
  <div>
    <div class="diagonal-box-top bg"></div>
    <!-- Top Toolbar -->
    <v-app-bar color="indigo" flat dark app dense scroll-threshold="128">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn text class="mx-1 text-capitalize hidden-sm-and-down" href="/"
        >About</v-btn
      >
      <v-btn
        text
        class="mx-1 text-capitalize hidden-sm-and-down"
        href="/profile"
        >Profile</v-btn
      >
      <v-btn
        text
        class="mx-1 text-capitalize hidden-sm-and-down"
        href="/projects"
        >Projects</v-btn
      >
    </v-app-bar>
    <!-- Nav Drawer -->
    <v-navigation-drawer v-model="drawer" temporary app>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="indigo--text">
          <v-list-item :value="true" href="/">
            <v-icon left>mdi-home</v-icon>
            <v-list-item-title>About</v-list-item-title>
          </v-list-item>
          <v-list-item href="/profile">
            <v-icon left>mdi-account</v-icon>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item>
          <v-list-item href="/projects">
            <v-icon left>mdi-folder</v-icon>
            <v-list-item-title>Projects</v-list-item-title>
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
