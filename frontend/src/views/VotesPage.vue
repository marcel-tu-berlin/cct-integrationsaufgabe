<script setup>
import { onMounted, ref } from 'vue'

import { useVotesStore } from '@/stores/votes'

const votesStore = useVotesStore()

onMounted(() => {
  votesStore.fetchVotes()
})
</script>

<template></template>
