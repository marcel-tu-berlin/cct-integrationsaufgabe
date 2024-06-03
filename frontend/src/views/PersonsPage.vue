<script setup>
import { ref, onMounted } from 'vue'

import { usePersonsStore } from '../stores/persons'

import { useUserStore } from '@/stores/user'

import { storeToRefs } from 'pinia'

const { persons } = storeToRefs(usePersonsStore())

const { fetchPersons, createPerson, deletePerson } = usePersonsStore()

const userStore = useUserStore()

const loading = ref(false)

loading.value = true

const itemsPerPage = 10

const headers = ref([
  { title: 'ID', key: 'id' },
  { title: 'Name', key: 'full_name' },
  { title: 'Alter', key: 'age' },
  { title: 'Geschlecht', key: 'sex' },
  { title: 'Aktionen', key: 'actions', sortable: false }
])

const dialog = ref(false)
const dialogDelete = ref(false)

const newPerson = ref({
  fullName: '',
  age: 0,
  sex: ''
})

const personToDelete = ref(null)

const showAlert = ref(false)
const alertMessage = ref('')

async function save() {
  try {
    await createPerson(newPerson.value)
    close()
  } catch (error) {
    close()
    showAlert.value = true
    alertMessage.value = error.message
  }
}

function close() {
  dialog.value = false

  newPerson.value = {
    fullName: '',
    age: 0,
    sex: ''
  }
}

function closeDelete() {
  dialogDelete.value = false
}

async function deleteItemConfirm() {
  dialogDelete.value = false
  try {
    await deletePerson(personToDelete.value)
  } catch (error) {
    showAlert.value = true
    alertMessage.value = error.message
  }
}

function deleteItem(item) {
  personToDelete.value = item
  dialogDelete.value = true
}

onMounted(() => {
  fetchPersons().then(() => {
    loading.value = false
  })
})
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-text>
            <v-alert
              v-model="showAlert"
              type="error"
              closable
              border="start"
              elevation="2"
              icon="mdi-alert"
            >
              {{ alertMessage }}
            </v-alert>
            <v-data-table
              :items="persons"
              :loading="loading"
              :items-per-page="itemsPerPage"
              :headers="headers"
              :sort-by="[{ key: 'id', direction: 'asc' }]"
            >
              <template #loading>
                <v-skeleton-loader :type="`table-row@${itemsPerPage}`"></v-skeleton-loader>
              </template>

              <template #top>
                <v-toolbar flat>
                  <v-toolbar-title>Personenverwaltung</v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>

                  <v-spacer></v-spacer>

                  <v-dialog v-model="dialog" max-width="290">
                    <template #activator="{ props }">
                      <v-btn color="primary" dark v-bind="props">Neue Person</v-btn>
                    </template>

                    <v-card>
                      <v-card-title>
                        <span class="text-h5">Neue Person</span>
                      </v-card-title>

                      <v-card-text>
                        <v-form>
                          <v-text-field
                            v-model="newPerson.fullName"
                            label="Name"
                            required
                          ></v-text-field>

                          <v-text-field
                            v-model="newPerson.age"
                            label="Alter"
                            required
                            type="number"
                          ></v-text-field>

                          <v-select
                            label="Geschlecht"
                            :items="['M', 'F', 'D']"
                            v-model="newPerson.sex"
                          ></v-select>
                        </v-form>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="close">Abbrechen</v-btn>
                        <v-btn color="blue-darken-1" variant="text" @click="save">Speichern</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>

                  <v-dialog v-model="dialogDelete" max-width="500px">
                    <v-card>
                      <v-card-title class="text-h5"
                        >Sind Sie sicher, dass Sie den Eintrag löschen möchten?</v-card-title
                      >
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="closeDelete"
                          >Abbrechen</v-btn
                        >
                        <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm"
                          >OK</v-btn
                        >
                        <v-spacer></v-spacer>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>

              <template #item.actions="{ item }">
                <v-icon size="small" @click="deleteItem(item)">mdi-delete</v-icon>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
