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
        <ul>
          <li><b>Salud general autopercibida:</b> La percepción personal de la salud está vinculada a factores físicos y emocionales que pueden influir en el riesgo de enfermedades crónicas.</li>
          <li><b>Días con mala salud física (último mes):</b> Una mayor cantidad de días con malestar físico puede estar asociada a patologías subyacentes, incluyendo riesgo de diabetes.</li>
          <li><b>Días con mala salud mental (último mes):</b> El estrés, la ansiedad y la depresión se han relacionado con una mayor probabilidad de alteraciones metabólicas y riesgo de diabetes.</li>
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
