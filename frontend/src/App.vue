<script setup>
import { useUserStore } from './stores/user'

const userStore = useUserStore()

const appTitle = import.meta.env.VITE_APP_TITLE
</script>

<template>
  <v-app>
    <v-app-bar scroll-behavior="elevate">
      <template #prepend>
        <img src="/favicon.png" alt="Logo" height="40" width="40" />
      </template>

      <v-app-bar-title>{{ appTitle }}</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn variant="text" to="/">Home</v-btn>
      <v-btn variant="text" to="/about">About</v-btn>
      <v-btn variant="text" to="/contact">Kontakt</v-btn>

      <v-btn variant="text" to="/login" color="primary" v-if="!userStore.user">Login</v-btn>
      <v-btn variant="text" @click="userStore.logout" color="primary" v-else>Logout</v-btn>
    </v-app-bar>

    <v-navigation-drawer expand-on-hover rail>
      <template v-if="userStore.user">
        <v-list>
          <v-list-item
            prepend-icon="mdi-account-circle-outline"
            :title="`${userStore.user?.full_name}`"
          >
            <v-list-item-subtitle>
              {{ userStore.user?.email }}
            </v-list-item-subtitle>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>
      </template>
      <v-list>
        <v-list-item
          prepend-icon="mdi-account-group-outline"
          title="Personenverwaltung"
          to="/persons"
        />
        <v-list-item prepend-icon="mdi-vote-outline" title="Abstimmungen" to="/positions" />
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
