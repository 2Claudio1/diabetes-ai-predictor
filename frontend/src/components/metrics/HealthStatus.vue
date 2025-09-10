<template>
  <div class="form-container">
    <div class="form-section">
      <div class="iframe-wrapper">
        <iframe
          class="powerbi-frame"
          title="Dashboard TFM Características del Modelo"
          src="https://app.powerbi.com/view?r=eyJrIjoiYTI5OWU3NDktZjE4My00MTY2LThhMTgtMTRlY2UzNzE0NWY1IiwidCI6IjAzNWZkZjQ0LTA2ODctNDFjOS04NGNjLTgwNmNlZDIxNzdiOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>

      <div class="info-text">
        <h3>Sobre las Variables de Estado de Salud</h3>
        <p>
          El estado de salud autopercibido y las experiencias recientes de malestar físico o mental son variables importantes para comprender la calidad de vida y posibles factores asociados al riesgo de diabetes. En esta sección se incluyen:
        </p>
        <ul class="my-4">
          <li><b>Nivel de actividad física habitual:</b> La práctica regular de ejercicio reduce el riesgo de resistencia a la insulina y de aparición de diabetes.</li>
          <li><b>Actividad física ≥ 300 min/semana:</b> Alcanzar este nivel semanal se asocia con una disminución significativa del riesgo metabólico.</li>
          <li><b>Fortalecimiento muscular ≥ 2 días/semana:</b> Las actividades de fuerza mejoran la sensibilidad a la insulina y el control glucémico.</li>
          <li><b>Frecuencia de consumo de frutas:</b> Una dieta rica en frutas aporta fibra y micronutrientes protectores frente a enfermedades metabólicas.</li>
          <li><b>Frecuencia de consumo de verduras:</b> Las verduras contribuyen a mantener un peso saludable y a prevenir complicaciones metabólicas.</li>
        </ul>
        <p>
          Analizar estas variables ayuda a valorar la dimensión subjetiva de la salud, un aspecto relevante para la predicción y prevención de la diabetes tipo 2.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "@/assets/metricsStyles.css";
</style>
