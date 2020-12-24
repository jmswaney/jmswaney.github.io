<template>
  <v-container style="margin-top: -192px" class="py-0">
    <!-- <v-card
      rounded="circle"
      color="indigo"
      elevation="18"
      class="mx-auto"
      max-width="220"
    >
      <v-avatar width="50%" height="auto">
        <v-img src="images/profile.jpg"></v-img>
      </v-avatar>
    </v-card> -->
    <v-row justify="center">
      <v-avatar width="50%" height="auto" class="elevation-15">
        <v-img src="images/profile.jpg"></v-img>
      </v-avatar>
    </v-row>

    <v-row justify="center">
      <v-col cols="auto" class="text-center">
        <h1>
          <span class="font-weight-light tw-text-3xl">Justin </span>
          <span class="indigo--text tw-text-3xl">Swaney</span>
        </h1>
        <p>
          <em>Scientist, Developer, Engineer</em>
          <br />
          <v-icon color="indigo lighten-2" class="px-5">mdi-microscope</v-icon>
          <v-icon color="indigo lighten-2" class="px-5"
            >mdi-laptop-windows</v-icon
          >
          <v-icon color="indigo lighten-2" class="px-5">mdi-flask</v-icon>
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
