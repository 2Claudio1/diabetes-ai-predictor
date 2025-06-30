<script setup lang="ts">
import { ref } from 'vue';
import { useForm, useField } from "vee-validate";
import * as yup from "yup";
import Dropdown from 'primevue/dropdown';
import InputNumber from 'primevue/inputnumber';
import Button from 'primevue/button';


const { errors, handleSubmit, useFieldModel } = useForm();

// Datos del formulario
const form = ref({
  sexo: null,
  grupo_edad: null,
  grupo_racial: null,
  nivel_educativo: null,
  categoria_ingresos: null,
  altura: null,
  peso: null,
  presion_alta: null,
  colesterol_alto: null,
  historial_acv: null,
  historial_cardiaco: null,
  dificultad_caminar: null,
  fumo_100_cigs: null,
  actividad_fisica: null,
  actividad_300min: null,
  actividad_muscular: null,
  frecuencia_frutas: null,
  frecuencia_verduras: null,
  salud_general: null,
  dias_mala_salud_fisica: null,
  dias_mala_salud_mental: null
});

// Función para calcular BMI
const calcularBMI = () => {
  if (form.value.altura && form.value.peso) {
    const alturaMetros = (+form.value.altura) / 100;
    const peso = +form.value.peso;
    return (peso / (alturaMetros * alturaMetros)).toFixed(2);
  }
  return null;
};

// Opciones para selects

// Sexo: 1 = Hombre, 0 = Mujer (coherente con datos)
const genderOptions = [
  { label: 'Masculino', value: 1 },
  { label: 'Femenino', value: 0 }
];

// Grupo de edad: 1 a 13
const ageOptions = [
  { label: '18-24', value: 1 },
  { label: '25-29', value: 2 },
  { label: '30-34', value: 3 },
  { label: '35-39', value: 4 },
  { label: '40-44', value: 5 },
  { label: '45-49', value: 6 },
  { label: '50-54', value: 7 },
  { label: '55-59', value: 8 },
  { label: '60-64', value: 9 },
  { label: '65-69', value: 10 },
  { label: '70-74', value: 11 },
  { label: '75-79', value: 12 },
  { label: '80+', value: 13 }
];

// Grupo racial, con 6 = Other (coherente)
const raceOptions = [
  { label: 'Blanco / Caucásico', value: 1 },
  { label: 'Negro / Africano', value: 2 },
  { label: 'Hispano / Latino', value: 3 },
  { label: 'Asiático', value: 4 },
  { label: 'Indígena / Nativo', value: 5 },
  { label: 'Otro', value: 6 }
];

// Nivel educativo 1-6 (sin posgrado)
const educationOptions = [
  { label: 'Nunca asistió', value: 1 },
  { label: 'Primaria', value: 2 },
  { label: 'Secundaria incompleta', value: 3 },
  { label: 'Secundaria completa', value: 4 },
  { label: 'Universidad incompleta', value: 5 },
  { label: 'Título universitario', value: 6 }
];

// Ingresos 1-8
const incomeOptions = [
  { label: 'Bajo', value: 1 },
  { label: 'Medio', value: 2 },
  { label: 'Alto', value: 3 }
];

// Opciones binarios Sí/No: 1 = Sí, 0 = No
const yesNoOptions = [
  { label: 'Sí', value: 1 },
  { label: 'No', value: 0 }
];

// Actividad física (binaria: 1=presente, 0=ausente)
const activityOptions = [
  { label: 'Ninguna', value: 0 },
  { label: 'Moderada o Intensa', value: 1 }
];

// Frecuencia frutas y verduras - invertidos para coincidir con el dataset
// 1 = alta frecuencia, 4 = baja frecuencia
const frequencyOptions = [
  { label: 'Diariamente', value: 1 },
  { label: 'Frecuentemente', value: 2 },
  { label: 'Ocasionalmente', value: 3 },
  { label: 'Nunca', value: 4 }
];

// Salud general (1 = mala, 5 = excelente)
const healthOptions = [
  { label: 'Mala', value: 1 },
  { label: 'Regular', value: 2 },
  { label: 'Buena', value: 3 },
  { label: 'Muy buena', value: 4 },
  { label: 'Excelente', value: 5 }
];

const checkForm = async () => {
  handleSubmit(async (values) => {

    console.log('Values: ', values);
  })();
};
</script>


<template>
  <div class="form-container">
    <div class=" mb-6">
      <div class="my-6 text-center">
        <h1 class="text-3xl font-bold text-primary">Predictor de Riesgo de Diabetes</h1>
      </div>
      <p class="text-xl text-color-secondary mt-2">
        Esta herramienta evalúa su riesgo de diabetes basado en métricas de salud.
        <br>Los resultados son una estimación predictiva, no un diagnóstico médico.
      </p>
    </div>
    <form @submit.prevent="checkForm" enctype="form-data">
      <!-- Sección Datos Personales -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Datos Personales</h2>
        <div class="grid">
          <div class="field">
            <label>Sexo</label>
            <Dropdown v-model="form.sexo" :options="genderOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Grupo de edad</label>
            <Dropdown v-model="form.grupo_edad" :options="ageOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Grupo racial/étnico</label>
            <Dropdown v-model="form.grupo_racial" :options="raceOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Nivel educativo</label>
            <Dropdown v-model="form.nivel_educativo" :options="educationOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Nivel de ingresos</label>
            <Dropdown v-model="form.categoria_ingresos" :options="incomeOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
        </div>
      </div>

      <!-- Sección Biométrica -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Medidas Biométricas</h2>
        <div class="grid">
          <div class="field">
            <label>Altura (cm)</label>
            <InputNumber v-model="form.altura" mode="decimal" :min="100" :max="250" class="w-full" />
          </div>
          <div class="field">
            <label>Peso (kg)</label>
            <InputNumber v-model="form.peso" mode="decimal" :min="30" :max="300" class="w-full" />
          </div>
          <!-- <div class="field">
            <label>
              IMC (BMI)
              <i class="pi pi-info-circle ml-2"
                v-tooltip="'El IMC es un indicador del peso corporal en relación con la altura. Un IMC alto implica mayor riesgo de diabetes.'"></i>
            </label>
            <InputNumber :value="calcularBMI()" disabled class="w-full" />
          </div> -->
          <div class="field">
            <label>IMC (BMI)</label>
            <InputNumber :value="calcularBMI()" disabled class="w-full" />
          </div>
        </div>
      </div>

      <!-- Sección Historial Médico -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Historial Médico</h2>
        <div class="grid">
          <div class="field">
            <label>Presión arterial alta</label>
            <Dropdown v-model="form.presion_alta" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Colesterol alto</label>
            <Dropdown v-model="form.colesterol_alto" :options="yesNoOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Historial de ACV</label>
            <Dropdown v-model="form.historial_acv" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Historial cardíaco</label>
            <Dropdown v-model="form.historial_cardiaco" :options="yesNoOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Dificultad para caminar</label>
            <Dropdown v-model="form.dificultad_caminar" :options="yesNoOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Fumó más de 100 cigarrillos</label>
            <Dropdown v-model="form.fumo_100_cigs" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
        </div>
      </div>

      <!-- Sección Hábitos -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Hábitos y Estilo de Vida</h2>
        <div class="grid">
          <div class="field">
            <label>Nivel de actividad física</label>
            <Dropdown v-model="form.actividad_fisica" :options="activityOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>300+ min de actividad física semanal?</label>
            <Dropdown v-model="form.actividad_300min" :options="yesNoOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Cumple recomendación de fortalecimiento muscular?</label>
            <Dropdown v-model="form.actividad_muscular" :options="yesNoOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Frecuencia de consumo de frutas</label>
            <Dropdown v-model="form.frecuencia_frutas" :options="frequencyOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <label>Frecuencia de consumo de verduras</label>
            <Dropdown v-model="form.frecuencia_verduras" :options="frequencyOptions" optionLabel="label"
              placeholder="Seleccione" class="w-full" />
          </div>
        </div>
      </div>

      <!-- Sección Salud -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Estado de Salud</h2>
        <div class="grid">
          <div class="field">
            <label>Salud general autopercibida</label>
            <Dropdown v-model="form.salud_general" :options="healthOptions" optionLabel="label" placeholder="Seleccione"
              class="w-full" />
          </div>
          <div class="field">
            <label>Días con mala salud física (último mes)</label>
            <InputNumber v-model="form.dias_mala_salud_fisica" :min="0" :max="30" class="w-full" />
          </div>
          <div class="field">
            <label>Días con mala salud mental (último mes)</label>
            <InputNumber v-model="form.dias_mala_salud_mental" :min="0" :max="30" class="w-full" />
          </div>
        </div>
        <Button label="Enviar Datos" class="submit-button" />
      </div>

    </form>
  </div>
</template>



<style scoped>
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

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.submit-button {
  width: 100%;
  margin-top: 1.5rem;
  padding: 1rem;
}

h2 {
  color: green;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }

  .form-container {
    padding: 0.5rem;
  }
}
</style>