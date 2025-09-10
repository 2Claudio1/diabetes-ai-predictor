<script setup lang="ts">
import { ref, computed } from "vue";
import PersonalRecords from '@/components/metrics/PersonalRecords.vue'
import MedicalHistory from '@/components/metrics/MedicalHistory.vue'
import LifestyleHabits from '@/components/metrics/LifestyleHabits.vue'
import HealthStatus from '@/components/metrics/HealthStatus.vue'

const selectedPage = ref<number>(1);

const tabs = [
  { 
    id: 1, 
    name: 'Distribución Demográfica',
    title: 'Distribución Demográfica',
    subtitle: 'Edad, género y grupo étnico en la población de estudio'
  },
  { 
    id: 2, 
    name: 'Historial Médico',
    title: 'Indicadores Clínicos',
    subtitle: 'Condiciones médicas asociadas al riesgo de diabetes'
  },
  { 
    id: 3, 
    name: 'Hábitos',
    title: 'Patrones de Conducta',
    subtitle: 'Factores de riesgo modificables en el estilo de vida'
  },
  { 
    id: 4, 
    name: 'Estado de Salud',
    title: 'Mediciones Biométricas',
    subtitle: 'Indicadores físicos relacionados con la diabetes'
  }
];

const activeTab = computed(() => {
  return tabs.find(t => t.id === selectedPage.value)!;
});
</script>

<template>
  <div class="dashboard-container">
    <!-- Encabezado principal -->
    <div class="header-section">
      <h1 class="main-title">Variables Clave en Diabetes</h1>
      <p class="description">
        Estas métricas muestran los patrones del dataset utilizado para entrenar nuestro modelo predictivo.
      </p>
    </div>

    <!-- Bloque Tabs + Título -->
    <div class="tab-container">
      <div class="tab-header">
        <button 
          v-for="tab in tabs" 
          :key="tab.id" 
          @click="selectedPage = tab.id"
          :class="['tab-button', { active: selectedPage === tab.id }]"
        >
          {{ tab.name }}
        </button>
      </div>
      <div class="tab-content">
        <h2>{{ activeTab.title }}</h2>
        <p>{{ activeTab.subtitle }}</p>
      </div>
    </div>

    <!-- Contenido precargado -->
    <div class="content-wrapper">
      <div v-show="selectedPage === 1" class="section-container">
        <PersonalRecords />
      </div>
      <div v-show="selectedPage === 2" class="section-container">
        <MedicalHistory />
      </div>
      <div v-show="selectedPage === 3" class="section-container">
        <LifestyleHabits />
      </div>
      <div v-show="selectedPage === 4" class="section-container">
        <HealthStatus />
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.header-section {
  text-align: center;
  margin: 2rem 0;
}

.main-title {
  font-size: 1.8rem;
  font-weight: 600;
  color: #16a34a;
  margin-bottom: 0.5rem;
}

.description {
  color: #4b5563;
  font-size: 1.1rem;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto 1.5rem;
}

.tab-container {
  background: #f9fafb;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.tab-header {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.tab-button {
  border: none;
  background: #e5e7eb;
  color: #4b5563;
  padding: 0.5rem 1.2rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.95rem;
}

.tab-button.active {
  background: #16a34a;
  color: white;
}

.tab-content h2 {
  color: #16a34a;
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
}

.tab-content p {
  color: #6b7280;
  font-size: 0.95rem;
}

.section-container {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  margin-bottom: 2rem;
}

.content-wrapper {
  transition: opacity 0.3s ease;
}

@media (max-width: 768px) {
  .tab-header {
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  
  .tab-button {
    flex: 1 0 calc(50% - 0.5rem);
  }
}

@media (max-width: 480px) {
  .main-title {
    font-size: 1.6rem;
  }
  .description {
    font-size: 1rem;
  }
  .tab-content h2 {
    font-size: 1.3rem;
  }
}
</style>
