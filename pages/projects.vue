<template>
  <v-row justify="center" style="margin-top: -192px" class="py-0">
    <v-col cols="auto">
      <v-card flat max-width="420" class="mx-2 transparent">
        <v-img width="100%" src="/images/organoid_blender.jpg" class="mx-auto">
        </v-img>
        <v-card-title class="headline">
          <em>SCOUT</em>ing mini-brains
        </v-card-title>
        <v-card-text class="tw-prose">
          <p>
            Published in <em>Scientific Reports</em>, the SCOUT pipeline enables
            rapid staining, imaging, and analysis of 3D cerebral organoids. We
            applied SCOUT to compare different culture protocols as well as to
            study how Zika virus inhibits organoid growth.
          </p>
          <p>
            SCOUT's computational pipeline is a Python package with a pre-built
            Docker image. The package also includes a pre-trained U-Net model
            for segmentation of ventricular zones in cerebral organoids based
            solely on nuclear staining.
          </p>
          <hr class="my-3" />
          <template v-for="link of links">
            <v-icon :key="link.name">{{ link.icon }}</v-icon>
            <a :key="link.name" :href="link.href">
              {{ link.name }}
            </a>
            <br :key="link.name" />
          </template>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      links: [
        {
          name: 'MIT News Article',
          icon: 'mdi-newspaper-variant',
          href:
            'https://news.mit.edu/2020/scout-helps-researchers-find-quantify-differences-among-organoids-1214',
        },
        {
          name: 'Publications (Open Access)',
          icon: 'mdi-book-open-blank-variant',
          href: 'https://www.nature.com/articles/s41598-020-78130-7',
        },
        {
          name: 'Github Repo',
          icon: 'mdi-github',
          href: 'https://github.com/chunglabmit/scout',
        },
      ],
    }
  },
})
</script>
