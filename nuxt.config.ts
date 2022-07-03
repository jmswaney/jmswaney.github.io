import { defineNuxtConfig } from 'nuxt'


// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  modules: ['@nuxt/content'],
  build: {},
  css: ['mdi/css/materialdesignicons.min.css'],
  content: {
    documentDriven: true
  }
})
