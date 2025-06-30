<template>
    <label class="flex items-center gap-2 font-medium">
      <span>{{ label }}</span>
      <i v-if="tooltip" class="pi pi-info-circle text-primary cursor-help" v-tooltip.right="tooltip"></i>
    </label>
  </template>
  
  <script setup lang="ts">
  defineProps<{
    label: string
    tooltip?: string
  }>()
  </script>
  