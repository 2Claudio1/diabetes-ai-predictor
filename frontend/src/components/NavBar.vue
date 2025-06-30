<script setup lang="ts">
import { RouterLink } from 'vue-router'

const navItems = [
  { label: 'Inicio', path: '/' },
  { label: 'Test Diabetes', path: '/teste-diabetes' }, // Versión equilibrada
  { label: 'Métricas', path: '/metricas-diabetes' },
  { label: 'Análisis Global', path: '/analisis-global' } // Versión equilibrada
]
</script>

<template>
  <nav class="navbar">
    <div class="nav-container">
      <RouterLink 
        v-for="item in navItems" 
        :key="item.path"
        :to="item.path"
        class="nav-link"
      >
        {{ item.label }}
      </RouterLink>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background: #2c3e50;
  padding: 0.5rem 0;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  padding: 0 0.5rem;
  overflow-x: auto;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none; /* Para Firefox */
}

.nav-container::-webkit-scrollbar {
  display: none; /* Para Chrome/Safari */
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.6rem 0.8rem;
  border-radius: 4px;
  font-size: 0.9rem;
  transition: all 0.2s;
  flex-shrink: 0;
  text-align: center;
  min-width: max-content;
}

.nav-link:hover {
  background: rgba(255,255,255,0.15);
}

.nav-link.router-link-exact-active {
  background: #3498db;
  font-weight: 500;
}

@media (max-width: 480px) {
  .nav-container {
    justify-content: flex-start;
    padding: 0.5rem;
  }
  
  .nav-link {
    padding: 0.5rem 0.7rem;
    font-size: 0.85rem;
  }
}

@media (min-width: 481px) and (max-width: 768px) {
  .nav-link {
    padding: 0.5rem 0.7rem;
    font-size: 0.88rem;
  }
}
</style>