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

      <v-btn variant="text" to="/login" color="primary">Login</v-btn>
    </v-app-bar>

    <v-navigation-drawer expand-on-hover rail>
      <v-list>
        <v-list-item
          prepend-icon="mdi-account-circle-outline"
          :title="`${userStore.user?.firstName} ${userStore.user?.lastName}`"
        >
          <v-list-item-subtitle>
            <v-btn @click="userStore.logout" color="primary" variant="text" size="x-small"
              >Logout</v-btn
            >
          </v-list-item-subtitle>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          prepend-icon="mdi-account-group-outline"
          title="Personenverwaltung"
          to="/persons"
        />
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
