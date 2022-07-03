import { defineNuxtConfig } from 'nuxt'


// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  modules: ['@nuxt/content'],
  build: {
    transpile: ['vuetify']
  },
  css: ['vuetify/lib/styles/main.sass', 'mdi/css/materialdesignicons.min.css'],
  content: {
    documentDriven: true
  },
  vite: {
    define: {
      'process.env.DEBUG': false,
    },
  }
})
