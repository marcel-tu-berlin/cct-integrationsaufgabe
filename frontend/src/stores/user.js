import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)

  function login(username, password) {
    console.log('Logging in', username, password)
  }

  return { user, login }
})
