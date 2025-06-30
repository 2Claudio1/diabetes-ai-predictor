<script setup lang="ts">





</script>

<template>
  <div class="form-container">
    <div class=" mb-6">
      <div class="my-6 text-center">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Valores del Dataset Inicial</h2>
        <div class="grid">
        </div>
      </div>
    </div>
    <div class="form-section">
      <!-- <iframe title="Dashboard TFM Metricas de Uso"  width="1280" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiNmY3NTUxZjEtYWFmYi00MzA3LThjNGMtMTE4NDJkMTljYTgyIiwidCI6IjAzNWZkZjQ0LTA2ODctNDFjOS04NGNjLTgwNmNlZDIxNzdiOCJ9" frameborder="0" allowFullScreen="true"></iframe> -->
      <iframe class="desktop" title="Dashboard TFM Características del Modelo" src="https://app.powerbi.com/view?r=eyJrIjoiNTU1NGM4ODAtZjFkMy00Njg0LWJlMzAtNDJiNDhjYTBkNTZiIiwidCI6IjAzNWZkZjQ0LTA2ODctNDFjOS04NGNjLTgwNmNlZDIxNzdiOCJ9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
  </div>
</template>

<style scoped>

.desktop{
  width: 1120px;
  height:600px;
}

.mobile{
  width: 320px;
  height:250px;
}

.form-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.form-section {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: var(--surface-card);
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-section h2 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
}
</style>