import { useContext, ref, useFetch } from '@nuxtjs/composition-api'

export const useProject = (path: string) => {
  const { app } = useContext()
  const project = ref(null)
  const { fetch } = useFetch(async () => {
    project.value = await app.$content(path).fetch()
  })
  fetch()
  return { project }
}
