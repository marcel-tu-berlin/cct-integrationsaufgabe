<script setup>
import { ref } from 'vue'
import { useUserStore } from '../stores/user'
import { useRouter } from 'vue-router'

const router = useRouter()

const userStore = useUserStore()

const username = ref('')
const password = ref('')

const showAlert = ref(false)
const showPassword = ref(false)

const login = () => {
  try {
    userStore.login(username.value, password.value)
    router.push('/')
  } catch (error) {
    reset()
    showAlert.value = true

    setTimeout(() => {
      showAlert.value = false
    }, 3000)
  }
}

const form = ref(null)

const reset = () => {
  form.value.reset()
}

const usernameRules = [
  (v) => !!v || 'Benutzername ist erforderlich',
  (v) => (v && v.length <= 100) || 'Benutzername darf nicht länger als 100 Zeichen sein'
]

const passwordRules = [(v) => !!v || 'Passwort ist erforderlich']
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <v-sheet rounded elevation="2" class="pa-4">
          <v-alert v-model="showAlert" type="error" dismissible>
            Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre Anmeldeinformationen.
          </v-alert>
          <h1>Login</h1>
          <p class="mb-3">Bitte melden Sie sich an, um das Wahlsystem zu nutzen.</p>
          <v-form @submit.prevent="login" ref="form">
            <v-text-field
              label="Benutzername"
              v-model="username"
              class="mt-1"
              :rules="usernameRules"
            ></v-text-field>
            <v-text-field
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              label="Passwort"
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              class="mb-1"
              :rules="passwordRules"
            ></v-text-field>
            <v-btn @click="reset" class="my-1" variant="text" block>Zurücksetzen</v-btn>
            <v-btn type="submit" block class="mt-1" color="primary">Anmelden</v-btn>
          </v-form>

          <v-divider class="my-4"></v-divider>

          <v-tooltip>
            <template #activator="{ props }">
              <v-btn block color="primary" :="props" to="/register">Registrieren</v-btn>
            </template>
            <span>Erstellen Sie ein neues Konto</span>
          </v-tooltip>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>
