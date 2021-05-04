<template>
  <v-row justify="center" style="margin-top: -192px" class="py-0">
    <v-col cols="auto">
      <v-card flat max-width="360" class="mx-2 transparent">
        <v-img width="100%" src="/images/organoid_blender.jpg" class="mx-auto">
        </v-img>
        <v-card-title class="headline pb-0">
          {{ scout.title }}
        </v-card-title>
        <v-card-text class="tw-prose">
          <nuxt-content :document="scout"></nuxt-content>
          <template v-for="link of scout.links">
            <v-icon :key="`icon-${link.name}`">{{ link.icon }}</v-icon>
            <a :key="link.name" :href="link.href">
              {{ link.name }}
            </a>
            <br :key="`br-${link.name}`" />
          </template>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import {
  defineComponent,
  useContext,
  ref,
  useFetch,
} from '@nuxtjs/composition-api'

export default defineComponent({
  setup() {
    const { app } = useContext()
    const scout = ref(null)
    const { fetch } = useFetch(async () => {
      scout.value = await app.$content('projects/scout').fetch()
    })
    fetch()
    return { scout }
  },
})
</script>
