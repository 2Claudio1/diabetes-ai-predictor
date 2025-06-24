<template>
    <Menubar :model="items">
      <template #start>
        <span class="text-xl font-bold">Diabetes Predictor</span>
      </template>
    </Menubar>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import type { MenuItem } from 'primevue/menuitem'
  
  const items = ref<MenuItem[]>([
    { label: 'Inicio', icon: 'pi pi-home', to: '/' },
    { label: 'Reportes', icon: 'pi pi-chart-bar', to: '/reportes' }
  ])
  </script>