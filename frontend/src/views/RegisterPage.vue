<script setup>
import { ref } from 'vue'
import { useUserStore } from '../stores/user'
import { useRouter } from 'vue-router'

const router = useRouter()

const userStore = useUserStore()

const username = ref('')
const password = ref('')
const passwordConfirmation = ref('')
const email = ref('')
const fullName = ref('')

const showAlert = ref(false)
const showPassword = ref(false)

const register = () => {
  try {
    userStore.register(username.value, password.value, email.value, fullName.value)
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
  (v) => (v && v.length <= 100) || 'Benutzernamen dürfen nicht länger als 100 Zeichen sein'
]

const passwordRules = [(v) => !!v || 'Passwort ist erforderlich']

const passwordConfirmationRules = [
  (v) => !!v || 'Passwort bestätigen ist erforderlich',
  (v) => v === password.value || 'Passwörter stimmen nicht überein'
]

const emailRules = [
  (v) => !!v || 'E-Mail ist erforderlich',
  (v) => /.+@.+\..+/.test(v) || 'E-Mail muss gültig sein',
  (v) => (v && v.length <= 100) || 'E-Mail darf nicht länger als 100 Zeichen sein'
]

const fullNameRules = [
  (v) => !!v || 'Vollständiger Name ist erforderlich',
  (v) => (v && v.length <= 100) || 'Vollständiger Name darf nicht länger als 100 Zeichen sein'
]
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <v-sheet rounded elevation="2" class="pa-4">
          <v-alert v-model="showAlert" type="error" dismissible>
            Registrierung fehlgeschlagen. Bitte überprüfen Sie Ihre Registrierungsinformationen oder
            wenden Sie sich an den Administrator.
          </v-alert>
          <h1>Registrieren</h1>
          <p class="mb-3">Bitte registrieren Sie sich, um das Wahlsystem zu nutzen.</p>
          <v-form @submit.prevent="register" ref="form">
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
            <v-text-field
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="showPassword = !showPassword"
              label="Passwort bestätigen"
              :type="showPassword ? 'text' : 'password'"
              v-model="passwordConfirmation"
              class="mb-1"
              :rules="passwordConfirmationRules"
            ></v-text-field>
            <v-text-field
              label="E-Mail"
              v-model="email"
              class="mb-1"
              :rules="emailRules"
              type="email"
            ></v-text-field>
            <v-text-field
              label="Vollständiger Name"
              v-model="fullName"
              class="mb-1"
              :rules="fullNameRules"
            ></v-text-field>
            <v-btn @click="reset" class="my-1" variant="text" block>Zurücksetzen</v-btn>
            <v-btn type="submit" block class="mt-1" color="primary">Anmelden</v-btn>
          </v-form>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>
