// import { defineNuxtConfig } from 'nuxt'
import tailwindTypography from '@tailwindcss/typography'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default {
  modules: ['@nuxt/content', '@nuxtjs/tailwindcss'],
  build: {
    transpile: ["vuetify"]
  },
  css: ['mdi/css/materialdesignicons.min.css'],
  content: {
    documentDriven: true
  },
  tailwindcss: {
    config: {
      plugins: [tailwindTypography]
    }
  }
}
