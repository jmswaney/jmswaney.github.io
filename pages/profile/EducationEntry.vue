<template>
  <div>
    <h1 class="text-body-2">{{ level }} in {{ field }}</h1>
    <h1 class="pb-3 text-body-2 font-weight-medium">
      {{ school }}, {{ year }}
    </h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api'

interface EducationEntry {
  level: string
  field: string
  school: string
  year: number
}

export default defineComponent({
  props: {
    entry: {
      type: Object as () => EducationEntry,
      required: true,
    },
  },
  setup(props) {
    return {
      level: props.entry.level,
      field: props.entry.field,
      school: props.entry.school,
      year: props.entry.year,
    }
  },
})
</script>
