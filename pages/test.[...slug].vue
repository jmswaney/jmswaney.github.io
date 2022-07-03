<template>
  <main>
    <ContentDoc v-slot="{ doc }">
      <h1>{{ doc.description }}</h1>
      <ContentRenderer :value="doc" />
    </ContentDoc>
  </main>
</template>

<script setup>
console.log("Hello world!")
</script>
