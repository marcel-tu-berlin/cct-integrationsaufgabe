import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from './user'

const baseURL = import.meta.env.VITE_API_URL

export const useVoteStore = defineStore('votes', () => {
  const votes = ref([])

  async function fetchVotes() {
	const response = await fetch(`${baseURL}/votes`, {
		headers: { Authorization: `Bearer ${useUserStore().user.token}` },
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	votes.value = data
  }

  return { votes, fetchVotes }
}, { persist: true })
