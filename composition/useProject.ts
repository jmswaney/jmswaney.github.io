import { useContext, ref, useFetch } from '@nuxtjs/composition-api'

export const useContent = (path: string) => {
  const { app } = useContext()
  const data = ref(null)
  const { fetch } = useFetch(async () => {
    data.value = await app.$content(path).fetch()
    console.log(data.value)
  })
  fetch()
  return data
}
