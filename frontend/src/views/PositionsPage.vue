<script setup>
import { onMounted, ref } from 'vue'

import { usePositionsStore } from '@/stores/positions'
import { useVotesStore } from '@/stores/votes'
import { usePersonsStore } from '@/stores/persons'

const positionsStore = usePositionsStore()
const votesStore = useVotesStore()
const personsStore = usePersonsStore()

const headers = ref([
  { title: 'ID', key: 'id' },
  { title: 'Titel', key: 'name' },
  { title: 'Beschreibung', key: 'description' }
])

const itemsPerPage = ref(10)
const itemsPerPageVotes = ref(10)
const expanded = ref([])

const reduceVotes = (votes) => {
  const reducedVotes = votes.reduce((acc, vote) => {
    console.log(acc, vote)
    if (!acc[vote.person_id]) {
      acc[vote.person_id] = 0
    }

    acc[vote.person_id]++

    return acc
  }, {})

  const votedPersons = Object.keys(reducedVotes)
  return votedPersons.map((personId) => {
    const person = personsStore.persons.find((person) => person.id === parseInt(personId))
    return {
      name: person.full_name,
      votes: reducedVotes[personId],
      percentage: `${(reducedVotes[personId] / votes.length) * 100}%`
    }
  })
}

const dialog = ref(false)
const newVote = ref({
  position: null,
  person: null
})

const createVote = () => {
  votesStore.createVote(newVote.value.position.id, newVote.value.person.id)
  close()
}

const close = () => {
  dialog.value = false

  newVote.value.position = null
  newVote.value.person = null
}

onMounted(() => {
  positionsStore.fetchPositions()
  votesStore.fetchVotes()
  personsStore.fetchPersons()
})
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="positionsStore.positions"
              :items-per-page="itemsPerPage"
              v-model:expanded="expanded"
              show-expand
            >
              <template v-slot:expanded-row="{ columns, item }">
                <tr>
                  <td :colspan="columns.length">
                    <v-card>
                      <v-card-title>Abstimmungen für: {{ item.name }}</v-card-title>
                      <v-card-text>
                        <v-data-table
                          :headers="[
                            { title: 'Name', key: 'name' },
                            { title: 'Stimmen', key: 'votes' },
                            { title: 'Prozent', key: 'percentage' }
                          ]"
                          :items="reduceVotes(item.votes)"
                          :items-per-page="itemsPerPageVotes"
                        >
                        </v-data-table>
                      </v-card-text>
                    </v-card>
                  </td>
                </tr>
              </template>

              <template #top>
                <v-toolbar flat>
                  <v-toolbar-title>Abstimmungen</v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>

                  <v-spacer></v-spacer>

                  <v-dialog v-model="dialog" max-width="290">
                    <template #activator="{ props }">
                      <v-btn color="primary" dark v-bind="props">Wählen</v-btn>
                    </template>

                    <v-card>
                      <v-card-title>
                        <span class="text-h5">Neue Person</span>
                      </v-card-title>

                      <v-card-text>
                        <v-form>
                          <v-select
                            label="Position"
                            :items="positionsStore.positions"
                            v-model="newVote.position"
                            item-title="name"
                            item-value="id"
                            return-object
                          ></v-select>

                          <v-select
                            label="Person"
                            :items="personsStore.persons"
                            v-model="newVote.person"
                            item-title="full_name"
                            item-value="id"
                            return-object
                          ></v-select>
                        </v-form>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="close">Abbrechen</v-btn>
                        <v-btn color="blue-darken-1" variant="text" @click="createVote"
                          >Speichern</v-btn
                        >
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
