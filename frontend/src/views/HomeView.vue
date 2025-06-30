<script setup lang="ts">
import Button from 'primevue/button'
</script>

<template>
  <div class="flex justify-center my-8" style="justify-content: center;">
    <div class="surface-card p-5 border-round shadow-3 w-full max-w-2xl text-center" style="width: 80% !important;">
      <h1 class="text-3xl md:text-4xl font-bold text-primary mb-4">
        Descubra el Poder de la Prevención: Conozca su Riesgo de Diabetes Tipo 2
      </h1>

      <p class="text-base md:text-lg mb-4 text-color-secondary">
        Tome el primer paso proactivo hacia su bienestar. Nuestra herramienta de evaluación de riesgo,
        impulsada por tecnología de Machine Learning, le permite obtener una predicción orientativa
        sobre si tiene riesgo de desarrollar diabetes tipo 2.
      </p>

      <div class="text-left mb-6">
        <h2 class="text-xl font-semibold text-primary mb-3">¿Cómo funciona?</h2>
        <p class="text-base md:text-lg mb-3 text-color-secondary">
          En menos de 5 minutos, responda a un cuestionario simple sobre sus hábitos de vida y estado de salud.
          Nuestro modelo analizará sus datos para predecir si su perfil se asocia a un riesgo de diabetes.
        </p>

        <h2 class="text-xl font-semibold text-primary mb-3 mt-5">¿Qué hace que nuestra herramienta sea única?</h2>
        <p class="text-base md:text-lg mb-3 text-color-secondary">
          A diferencia de otras calculadoras, utilizamos un modelo de inteligencia artificial de última generación,
          optimizado con técnicas avanzadas. Este modelo procesa variables clave relacionadas con su estilo de vida,
          permitiéndole entender qué factores bajo su control, como la actividad física y la alimentación,
          pueden influir en su propensión a la diabetes.
        </p>

        <p class="text-base md:text-lg mb-3 text-color-secondary">
          Después de la predicción, obtendrá:
        </p>
        <ul class="list-disc pl-5 mb-4 text-color-secondary">
          <li>Su resultado de riesgo: "Sí" o "No".</li>
          <li>Una visualización interactiva que muestra el impacto de cada variable en su predicción.</li>
          <li>Estadísticas de uso de la herramienta, para ver cómo su perfil se compara con otros usuarios.</li>
        </ul>

        <h2 class="text-xl font-semibold text-primary mb-3 mt-5">Un Paso Crucial para la Detección Temprana</h2>
        <p class="text-base md:text-lg mb-3 text-color-secondary">
          Según la Organización Mundial de la Salud (OMS), la detección temprana es fundamental para manejar
          la diabetes y prevenir complicaciones graves. Nuestra herramienta es un aliado en este proceso,
          brindándole información valiosa que puede motivar un cambio positivo.
        </p>
      </div>

      <div class="border-t-1 border-gray-300 pt-4">
        <p class="text-base md:text-lg mb-3 text-color-secondary">
          <strong class="text-red-600">Aviso Importante:</strong> Este es un análisis orientativo.
          El resultado que obtiene no constituye un diagnóstico médico. Nuestro modelo, aunque tiene
          un alto nivel de precisión (superior al 85%), no es un sustituto de una consulta profesional.
          Si su resultado es "Sí", es crucial que acuda a un profesional de la salud para realizarse
          los exámenes clínicos correspondientes y obtener un diagnóstico certero.
        </p>
        <p class="text-xs md:text-sm text-color-secondary mt-4">
          Su información es anónima y puede ser utilizada
          para mejorar continuamente la precisión del modelo.
        </p>
        <div class="mt-4">
          <p class="text-xs md:text-sm text-color-secondary">
            Este proyecto ha sido desarrollado en el Máster en Big Data y Análisis de Datos de la
            Universidad Internacional de La Rioja (UNIR) por los alumnos:
          </p>
          <p class="text-xs md:text-sm text-color-secondary">Cláudio Duarte Lopes Henriques</p>
          <p class="text-xs md:text-sm text-color-secondary">Henry Martin Paulett Ramirez</p>
          <p class="text-xs md:text-sm text-color-secondary">Rafael Edgardo Malca Torrejon</p>
        </div>
      </div>

      <router-link to="/teste-diabetes">
        <Button label="Iniciar Evaluación" class="mt-5 w-full md:w-auto" />
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.list-disc li {
  margin-bottom: 0.5rem;
}
</style>