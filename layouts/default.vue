<template>
  <v-app>
    <!-- Top Toolbar -->
    <v-card flat>
      <v-toolbar color="indigo" dark extended flat>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </v-toolbar>
      <v-card
        rounded="circle"
        elevation="20"
        class="mx-auto"
        max-width="240"
        style="margin-top: -64px"
      >
        <v-avatar width="100%" height="auto" max-width="240">
          <v-img src="images/profile.jpg"></v-img>
        </v-avatar>
      </v-card>
    </v-card>
    <!-- Nav Drawer -->
    <v-navigation-drawer v-model="drawer" absolute bottom temporary>
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
    <v-content>
      <Nuxt />
    </v-content>
    <!-- Footer -->
    <v-divider></v-divider>
    <v-footer padless color="white">
      <v-col class="text-center" cols="12"
        >&copy; {{ new Date().getFullYear() }}</v-col
      >
    </v-footer>
  </v-app>
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
