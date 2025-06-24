<script setup lang="ts">
import { ref } from 'vue'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'

const text = ref('')
</script>

<template>
  <div class="m-6">
    <main>
      <div class="p-4 flex justify-content-center">
        <h1>HomeView</h1>
      </div>

    </main>
    <span>Hello PrimeVue</span>
    <div>
      <InputText v-model="text"></InputText>
      <p>{{ text }}</p>
    </div>
  </div>
</template>
