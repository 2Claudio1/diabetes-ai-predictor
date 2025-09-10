<template>
  <div class="form-container">
    <div class="form-section">
      <div class="iframe-wrapper">
        <iframe
          class="powerbi-frame"
          title="Dashboard TFM Características del Modelo"
          src="https://app.powerbi.com/view?r=eyJrIjoiMTEyZDZhNzItN2JkNi00MDIxLTgzMGQtNGZhNmJjZDgxZGQzIiwidCI6IjAzNWZkZjQ0LTA2ODctNDFjOS04NGNjLTgwNmNlZDIxNzdiOCJ9"
          frameborder="0"
          allowFullScreen="true"
        ></iframe>
      </div>

      <div class="info-text">
        <h3>Sobre las Variables de Historial Médico</h3>
        <p>
          El historial médico es un conjunto de factores clínicos que se asocian de manera significativa al riesgo de desarrollar diabetes tipo 2. Estas variables permiten entender posibles antecedentes de salud que incrementan la probabilidad de la enfermedad. En esta sección se incluyen:
        </p>
        <ul class="my-4">
          <li><b>Diagnóstico de hipertensión arterial:</b> La presión arterial alta es uno de los factores de riesgo más importantes relacionados con la diabetes.</li>
          <li><b>Diagnóstico de colesterol elevado:</b> Los niveles altos de colesterol están vinculados con problemas metabólicos que aumentan el riesgo de diabetes.</li>
          <li><b>Consumo de al menos 100 cigarrillos a lo largo de la vida:</b> El tabaquismo es un factor que contribuye al desarrollo de resistencia a la insulina y, por ende, eleva el riesgo de diabetes.</li>
          <li><b>Antecedentes de accidente cerebrovascular (ACV):</b> Sufrir un ACV indica alteraciones vasculares que pueden coexistir con diabetes no diagnosticada.</li>
          <li><b>Antecedentes de enfermedad cardíaca:</b> La presencia de enfermedades cardiovasculares se relaciona estrechamente con el síndrome metabólico y la diabetes.</li>
          <li><b>Dificultad para caminar o subir escaleras:</b> Esta limitación funcional puede estar asociada a problemas metabólicos o neurológicos derivados de diabetes o a factores de riesgo comunes.</li>
        </ul>
        <p>
          Todas estas variables forman parte del análisis de predicción para identificar individuos con mayor riesgo de diabetes tipo 2.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "@/assets/metricsStyles.css";
</style>
