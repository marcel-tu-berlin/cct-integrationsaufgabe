import { ref } from 'vue'
import { defineStore } from 'pinia'

const baseURL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  async function login(username, password) {
	const response = await fetch(`${baseURL}/auth/token`, {
	  method: 'POST',
	  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
	  body: new URLSearchParams({ username, password }),
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	user.value = { username, token: data.access_token }

	console.log(user.value)
	
  }

  function logout() {
	console.log('Logging out')
  }

  return { user, login, logout }
}, { persist: true })
