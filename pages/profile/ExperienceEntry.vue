<template>
  <div>
    <h1 class="text-body-2">{{ role }}</h1>
    <h1 class="text-body-2 font-weight-medium">
      {{ company }}
    </h1>
    <h1 class="pb-3 text-body-2">{{ start }} - {{ end || 'Present' }}</h1>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from '@nuxtjs/composition-api'

interface ExperienceEntryProps {
  role: string
  company: string
  start: number
  end?: number
}

export default defineComponent({
  props: {
    entry: {
      type: Object as PropType<ExperienceEntryProps>,
      required: true,
    },
  },
  setup(props) {
    return {
      role: props.entry?.role,
      company: props.entry?.company,
      start: props.entry?.start,
      end: props.entry?.end,
    }
  },
})
</script>
