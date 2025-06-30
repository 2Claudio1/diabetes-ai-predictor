<script setup lang="ts">
import Button from 'primevue/button'
</script>

<template>
  <div >

  <div class="flex justify-center my-8" style="justify-content: center;">
    <div class="surface-card p-5 border-round shadow-3 w-full max-w-2xl text-center" style="width: 80% !important; ">
      <h1 class="text-3xl md:text-4xl font-bold text-primary mb-4">
        Predictor de Riesgo de Diabetes
      </h1>
      <p class="text-base md:text-lg mb-3 text-color-secondary">
        Bienvenido a nuestra herramienta interactiva para calcular tu riesgo de desarrollar
        <strong>diabetes tipo 2</strong>. Solo necesitas ingresar información sobre tus hábitos de vida,
        estado de salud y datos personales.
      </p>
      <p class="text-base md:text-lg mb-3 text-color-secondary">
        Utilizamos técnicas avanzadas de <strong>Machine Learning</strong>, como el algoritmo
        <strong>XGBoost</strong>, para analizar tu información y ofrecerte una predicción aproximada.
      </p>
      <p class="text-base md:text-lg mb-3 text-color-secondary">
        <strong class="text-red-600">
          Importante:
        </strong> Este resultado es solo orientativo y <strong>no constituye un diagnóstico médico</strong>.
        Para un diagnóstico certero, acude siempre a un profesional de salud y realiza
        los exámenes clínicos correspondientes.
      </p>
      <p class="text-xs md:text-sm text-color-secondary mb-4">
        Proyecto desarrollado en el Máster en Big Data y Análisis de Datos de la
        Universidad Internacional de La Rioja (UNIR).
      </p>
      <router-link to="/teste-diabetes">
        <Button label="Iniciar Evaluación" class="mt-3 w-full md:w-auto" />
      </router-link>
    </div>
  </div>

  </div>
</template>
