import { ref } from 'vue'
import { defineStore } from 'pinia'

const baseURL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  async function fetchUser() {
	const response = await fetch(`${baseURL}/users/me`, {
	  headers: { Authorization: `Bearer ${user.value.token}` },
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	user.value = { ...user.value, ...data }
  }

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

	await fetchUser()
  }

  async function logout() {
	user.value = null
  }

  async function register(username, password, email, full_name) {
	const response = await fetch(`${baseURL}/auth/register`, {
	  method: 'POST',
	  headers: { 'Content-Type': 'application/json' },
	  body: JSON.stringify({ username, password, email, full_name }),
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	user.value = { username, token: data.access_token }

	await fetchUser()
}

  return { user, login, fetchUser, logout, register }
}, { persist: true })
