import { ref } from 'vue'
import { defineStore } from 'pinia'

export const usePersonsStore = defineStore('persons', () => {
  const persons = ref([])

  function fetchPersons() {
	console.log('Fetching persons')
  }

  return { persons, fetchPersons }
})
