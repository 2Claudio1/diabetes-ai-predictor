<script setup lang="ts">
import { RouterView } from 'vue-router';
import Header from '@/components/Header.vue';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
</script>

<template>
  <div class="app-layout">

    <Header />
    <NavBar />
    <main class="main-content">
      <RouterView />
    </main>
    <Footer />
  </div>
</template>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
  width: 100vw; /* Ocupa el 100% del viewport */
  max-width: 100%; /* Elimina cualquier límite máximo */
  margin: 0;
  padding: 0; /* Elimina paddings que puedan reducir el ancho */
}
</style>