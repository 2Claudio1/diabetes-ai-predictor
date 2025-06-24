<script setup lang="ts">
import { RouterLink } from 'vue-router'

const navItems = [
  { label: 'Inicio', path: '/' },
  { label: 'Test de Diabetes', path: '/teste-diabetes' },
  { label: 'Métricas', path: '/metricas-diabetes' },
  { label: 'Mapa Mundial', path: '/mapa-mundial' }
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
  background: #2c3e50; /* Azul oscuro */
  padding: 0.5rem 0;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 0.8rem;
  padding: 0 1rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-size: 0.9rem;
  transition: all 0.2s;
}

.nav-link:hover {
  background: rgba(255,255,255,0.15);
}

.nav-link.router-link-exact-active {
  background: #3498db; /* Azul más claro */
  font-weight: 500;
}
</style>