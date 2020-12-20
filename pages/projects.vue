<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card elevation="12">
        <v-img width="100%" src="images/organoid_blender.jpg"> </v-img>
        <v-card-title class="headline"> SCOUTing mini-brains </v-card-title>
        <v-card-text>
          <p>
            Our SCOUT pipeline for rapid staining, imaging, and analysis 3D
            cerebral organoids was recently published in
            <em>Scientific Reports</em>. We applied SCOUT to compare different
            culture protocols as well as to study how Zika virus inhibits growth
            in cerebral organoids.
          </p>
          <p>
            SCOUT's computational pipeline is a Python package with a pre-built
            Docker image for easy use on Windows, Mac, and Linux. The package
            also includes a pre-trained U-Net model for segmentation of
            ventricular zones in cerebral organoids based solely on nuclear
            staining.
          </p>
          <hr class="my-3" />
          <a
            href="https://news.mit.edu/2020/scout-helps-researchers-find-quantify-differences-among-organoids-1214"
            target="_blank"
            rel="noopener noreferrer"
          >
            SCOUT MIT News Article
          </a>
          <br />
          <a
            href="https://www.nature.com/articles/s41598-020-78130-7"
            target="_blank"
            rel="noopener noreferrer"
          >
            SCOUT Publication (Open Access)
          </a>
          <br />
          <a
            href="https://github.com/chunglabmit/scout"
            target="_blank"
            rel="noopener noreferrer"
          >
            SCOUT GitHub Repo
          </a>
          <br />
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
