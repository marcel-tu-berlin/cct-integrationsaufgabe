<script setup></script>

<template>
  <v-app>
    <v-app-bar scroll-behavior="elevate">
      <template #prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>

      <v-app-bar-title>Wahlsystem</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn variant="text" to="/">Home</v-btn>
      <v-btn variant="text" to="/about">About</v-btn>
      <v-btn variant="text" to="/contact">Kontakt</v-btn>

      <v-btn variant="text" to="/login" color="primary">Login</v-btn>
    </v-app-bar>

    <v-navigation-drawer>
      <v-list> </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<style scoped></style>
