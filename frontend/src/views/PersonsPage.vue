<script setup>
import { ref, onMounted } from 'vue'

import { usePersonsStore } from '../stores/persons'

import { storeToRefs } from 'pinia'

const { persons } = storeToRefs(usePersonsStore())

const { fetchPersons } = usePersonsStore()

const loading = ref(false)

loading.value = true

const itemsPerPage = 10

function openCreatePersonDialog() {
  console.log('openCreatePersonDialog')
}

onMounted(() => {
  fetchPersons()
})
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>Personenverwaltung</v-card-title>
          <v-card-text>
            <v-btn @click="openCreatePersonDialog" color="primary">Neue Person</v-btn>
            <v-data-table :items="persons" :loading="loading" :items-per-page="itemsPerPage">
              <template #loading>
                <v-skeleton-loader :type="`table-row@${itemsPerPage}`"></v-skeleton-loader>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
