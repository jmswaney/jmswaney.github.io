import { useContext, ref, useFetch, Ref } from '@nuxtjs/composition-api'

export default function useContent<T>(path: string) {
  const { app } = useContext()
  const data = ref(null) as Ref<T | null>
  const { fetch, fetchState } = useFetch(async () => {
    data.value = await app.$content(path).fetch()
  })
  fetch()
  return {
    data,
    fetchState
  }
}
