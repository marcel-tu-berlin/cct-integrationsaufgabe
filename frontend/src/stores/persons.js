import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useUserStore } from './user'

const baseURL = import.meta.env.VITE_API_URL

export const usePersonsStore = defineStore('persons', () => {
  const persons = ref([])

  async function fetchPersons() {
	const response = await fetch(`${baseURL}/persons`, {
		headers: { Authorization: `Bearer ${useUserStore().user.token}` },
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	persons.value = data
  }

  async function createPerson(person) {
	const rqBody = {
		full_name: person.fullName,
		age: person.age,
		sex: person.sex,
	}

	const response = await fetch(`${baseURL}/persons`, {
		method: 'POST',
		headers: {
			'Authorization': `Bearer ${useUserStore().user.token}`,
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(rqBody),
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	
	await fetchPersons()
  }

  async function deletePerson(person) {
	const response = await fetch(`${baseURL}/persons/${person.id}`, {
		method: 'DELETE',
		headers: { Authorization: `Bearer ${useUserStore().user.token}` },
	})
	const data = await response.json()
	if (!response.ok) {
	  throw new Error(data.detail)
	}
	
	await fetchPersons()
  }

  return { persons, fetchPersons, createPerson, deletePerson }
}, { persist: true })
