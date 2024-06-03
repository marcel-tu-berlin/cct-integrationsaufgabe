import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from './user'

const baseURL = import.meta.env.VITE_API_URL

export const useVotesStore = defineStore('votes', () => {
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

  async function createVote(position_id, person_id) {
	const response = await fetch(`${baseURL}/votes`, {
		method: 'POST',
		headers: {
			'Authorization': `Bearer ${useUserStore().user.token}`,
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({ position_id, person_id }),
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	
	await fetchVotes()
  }

  return { votes, fetchVotes, createVote }
}, { persist: true })
