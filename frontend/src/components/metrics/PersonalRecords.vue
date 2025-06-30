<template>
    <div class="form-container">
      <div class="form-section">
        <div class="iframe-wrapper">
          <iframe
            class="powerbi-frame"
            title="Dashboard TFM Características del Modelo"
            src="https://app.powerbi.com/view?r=eyJrIjoiMjUzMWQ5NmQtZjkxMC00ZDcxLTk3ODUtYTYyM2RlMTRjM2I3IiwidCI6IjAzNWZkZjQ0LTA2ODctNDFjOS04NGNjLTgwNmNlZDIxNzdiOCJ9"
            frameborder="0"
            allowFullScreen="true"
          ></iframe>
        </div>
  
        <div class="info-text">
          <h3>Sobre las Variables de Datos Personales</h3>
          <p>
            El análisis de datos personales permite identificar patrones demográficos asociados al riesgo de diabetes tipo 2. A continuación, se describen las variables incluidas en esta sección:
          </p>
          <ul>
            <li><b>Sexo:</b> Se analiza la prevalencia de la diabetes entre hombres y mujeres, dado que algunos estudios muestran diferencias en la incidencia y factores de riesgo según género.</li>
            <li><b>Grupo de edad:</b> El riesgo de diabetes aumenta con la edad. Por ello, se agrupan rangos etarios para examinar en qué franjas se concentran más casos.</li>
            <li><b>Grupo racial o étnico:</b> Determinados grupos étnicos presentan mayor predisposición genética o condiciones socioeconómicas que incrementan el riesgo de diabetes tipo 2.</li>
            <li><b>Nivel educativo:</b> El nivel de educación puede influir en el acceso a información sobre salud y en hábitos preventivos, siendo un factor indirecto en el riesgo de desarrollar diabetes.</li>
            <li><b>Nivel de ingresos:</b> Los ingresos económicos están relacionados con el acceso a cuidados médicos, alimentación saludable y estilos de vida, lo que puede impactar en la prevalencia de diabetes.</li>
            <li><b>Índice de Masa Corporal (IMC):</b> Es una medida que relaciona peso y altura. Un IMC elevado está asociado a un mayor riesgo de desarrollar diabetes tipo 2.</li>
          </ul>
          <p>
            Estas variables forman parte del conjunto de datos utilizado para entrenar el modelo predictivo y son clave para comprender la distribución demográfica del riesgo de diabetes en la población analizada.
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  @import "@/assets/metricsStyles.css";
  </style>
  