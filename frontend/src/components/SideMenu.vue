<template>
    <PanelMenu :model="items" class="w-full md:w-64" />
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import type { MenuItem } from 'primevue/menuitem'
  
  const items = ref<MenuItem[]>([
    {
      label: 'Gráficas',
      items: [
        { label: 'Riesgo por edad', command: () => updateChart('age') }
      ]
    }
  ])
  
  const updateChart = (type: string) => {
    // Lógica TypeScript aquí
  }
  </script>