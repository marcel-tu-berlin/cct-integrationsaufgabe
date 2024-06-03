import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from './user'

const baseURL = import.meta.env.VITE_API_URL

export const usePositionStore = defineStore('positions', () => {
  const positions = ref([])

  async function fetchPositions() {
	const response = await fetch(`${baseURL}/positions`, {
		headers: { Authorization: `Bearer ${useUserStore().user.token}` },
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	positions.value = data
  }

  return { positions, fetchPositions }
}, { persist: true })
