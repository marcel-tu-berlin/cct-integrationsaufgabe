import { ref } from 'vue'
import { defineStore } from 'pinia'

const baseURL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', () => {
  const user = ref({
	firstName: 'John',
	lastName: 'Doe',
  })

  async function login(username, password) {
	const response = await fetch(`${baseURL}/login`, {
	  method: 'POST',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  body: JSON.stringify({ username, password }),
	})
	
	if (response.ok) {
	  const data = await response.json()
	  user.value = data
	}

	return response.ok
  }

  function logout() {
	console.log('Logging out')
  }

  return { user, login, logout }
})
