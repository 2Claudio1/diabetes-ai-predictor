<script setup lang="ts">
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { computed, onMounted, ref } from 'vue';
import Dropdown from 'primevue/dropdown';
import InputNumber from 'primevue/inputnumber';
import Button from 'primevue/button';
import Tooltip from 'primevue/tooltip';
import InfoLabel from '@/components/shared/InfoLabel.vue';
import { countryOptions } from '@/data/countries';

const vTooltip = Tooltip;

interface DiabetesForm {
  sexo: number;
  grupo_edad: number;
  grupo_racial: number;
  nivel_educativo: number;
  ingresos_grupo: number;
  pais: string;
  bmi?: number; // Make optional
  presion_alta: number;
  colesterol_alto: number;
  historial_acv: number;
  historial_cardiaco: number;
  dificultad_caminar: number;
  fumo_100_cigs: number;
  actividad_fisica: number;
  actividad_300_min : number;
  actividad_muscular: number;
  frecuencia_frutas: number;
  frecuencia_verduras: number;
  salud_general: number;
  dias_mala_salud_fisica: number;
  dias_mala_salud_mental: number;
  continente?: string; // Make optional
}

const { handleSubmit } = useForm();
const loading = ref(false);
const error = ref<string | null>(null);
const prediction = ref<number | null>(null);
const formSubmitted = ref(false);

const { value: sexo, errorMessage: sexoError } = useField<number>('sexo', yup.number().required('Campo requerido'));
const { value: grupo_edad, errorMessage: grupo_edadError } = useField<number>('grupo_edad', yup.number().required('Campo requerido'));
const { value: grupo_racial, errorMessage: grupo_racialError } = useField<number>('grupo_racial', yup.number().required('Campo requerido'));
const { value: nivel_educativo, errorMessage: nivel_educativoError } = useField<number>('nivel_educativo', yup.number().required('Campo requerido'));
const { value: ingresos_grupo, errorMessage: ingresos_grupoError } = useField<number>('ingresos_grupo', yup.number().required('Campo requerido'));
const { value: pais, errorMessage: paisError } = useField<string>('pais', yup.string().required('Campo requerido'));
const { value: altura, errorMessage: alturaError } = useField<number>('altura', yup.number().required('Campo requerido').min(100, 'Mínimo 100 cm').max(250, 'Máximo 250 cm'));
const { value: peso, errorMessage: pesoError } = useField<number>('peso', yup.number().required('Campo requerido').min(30, 'Mínimo 30 kg').max(300, 'Máximo 300 kg'));
const { value: presion_alta, errorMessage: presion_altaError } = useField<number>('presion_alta', yup.number().required('Campo requerido'));
const { value: colesterol_alto, errorMessage: colesterol_altoError } = useField<number>('colesterol_alto', yup.number().required('Campo requerido'));
const { value: historial_acv, errorMessage: historial_acvError } = useField<number>('historial_acv', yup.number().required('Campo requerido'));
const { value: historial_cardiaco, errorMessage: historial_cardiacoError } = useField<number>('historial_cardiaco', yup.number().required('Campo requerido'));
const { value: dificultad_caminar, errorMessage: dificultad_caminarError } = useField<number>('dificultad_caminar', yup.number().required('Campo requerido'));
const { value: fumo_100_cigs, errorMessage: fumo_100_cigsError } = useField<number>('fumo_100_cigs', yup.number().required('Campo requerido'));
const { value: actividad_fisica, errorMessage: actividad_fisicaError } = useField<number>('actividad_fisica', yup.number().required('Campo requerido'));
const { value: actividad_300_min, errorMessage: actividad_300_minError } = useField<number>('actividad_300_min', yup.number().required('Campo requerido'));
const { value: actividad_muscular, errorMessage: actividad_muscularError } = useField<number>('actividad_muscular', yup.number().required('Campo requerido'));
const { value: frecuencia_frutas, errorMessage: frecuencia_frutasError } = useField<number>('frecuencia_frutas', yup.number().required('Campo requerido'));
const { value: frecuencia_verduras, errorMessage: frecuencia_verdurasError } = useField<number>('frecuencia_verduras', yup.number().required('Campo requerido'));
const { value: salud_general, errorMessage: salud_generalError } = useField<number>('salud_general', yup.number().required('Campo requerido'));
const { value: dias_mala_salud_fisica, errorMessage: dias_mala_salud_fisicaError } = useField<number>('dias_mala_salud_fisica', yup.number().required('Campo requerido').min(0, 'Mínimo 0 días').max(30, 'Máximo 30 días'));
const { value: dias_mala_salud_mental, errorMessage: dias_mala_salud_mentalError } = useField<number>('dias_mala_salud_mental', yup.number().required('Campo requerido').min(0, 'Mínimo 0 días').max(30, 'Máximo 30 días'));

const bmi = computed(() => {
  const alturaNum = Number(altura.value);
  const pesoNum = Number(peso.value);
  if (!alturaNum || !pesoNum) return 0;
  const alturaMetros = alturaNum / 100;
  return parseFloat((pesoNum / (alturaMetros * alturaMetros)).toFixed(2));
});

const genderOptions = [
  { label: 'Masculino', value: 1 },
  { label: 'Femenino', value: 0 }
];

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

const raceOptions = [
  { label: 'Blanco / Caucásico', value: 1 },
  { label: 'Negro / Africano', value: 2 },
  { label: 'Hispano / Latino', value: 3 },
  { label: 'Asiático', value: 4 },
  { label: 'Indígena / Nativo', value: 5 },
  { label: 'Otro', value: 6 }
];

const educationOptions = [
  { label: 'Nunca asistió', value: 1 },
  { label: 'Primaria', value: 2 },
  { label: 'Secundaria incompleta', value: 3 },
  { label: 'Secundaria completa', value: 4 },
  { label: 'Universidad incompleta', value: 5 },
  { label: 'Título universitario', value: 6 }
];

const incomeOptions = [
  { label: 'Bajo', value: 1 },
  { label: 'Medio', value: 2 },
  { label: 'Alto', value: 3 }
];

const yesNoOptions = [
  { label: 'Sí', value: 1 },
  { label: 'No', value: 0 }
];

const activityOptions = [
  { label: 'Ninguna', value: 0 },
  { label: 'Moderada o Intensa', value: 1 }
];

const frequencyOptions = [
  { label: 'Nunca', value: 4 },
  { label: 'Baja (1-2/semana)', value: 3 },
  { label: 'Media (3-6/semana)', value: 2 },
  { label: 'Alta (7+/semana)', value: 1 }
];

const healthOptions = [
  { label: 'Mala', value: 1 },
  { label: 'Regular', value: 2 },
  { label: 'Buena', value: 3 },
  { label: 'Muy buena', value: 4 },
  { label: 'Excelente', value: 5 }
];

const checkForm = handleSubmit(async (values) => {
  loading.value = true;
  error.value = null;

  try {
    // Cast values to DiabetesForm
    const formValues = values as DiabetesForm;
    
    const formData: DiabetesForm = {
      ...formValues,
      bmi: bmi.value,
      continente: 'Europa'
    };

    const response = await fetch('http://localhost:8000/api/guardar-datos/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });

    if (!response.ok) throw new Error('Error al guardar los datos');

    const result = await response.json();
    console.log('Datos guardados:', result);
    prediction.value = result;
    formSubmitted.value = true;

  } catch (err) {
    console.error('Error:', err);
    error.value = err instanceof Error ? err.message : 'Error desconocido';
  } finally {
    loading.value = false;
  }
});

/* onMounted(async () => {
  formSubmitted.value = true
  prediction.value = 0
}) */
</script>

<template>
  <div class="form-container">
    <div v-if="error" class="error-message">
      {{ error }}
    </div>

    <div class="my-6 text-center">
      <h1 class="text-3xl font-bold text-primary">Predictor de Riesgo de Diabetes</h1>
      <p class="text-xl text-color-secondary mt-2">
        Esta herramienta evalúa tu riesgo de diabetes tipo 2 basado en tus datos de salud y estilo de vida.<br>
        Los resultados son solo orientativos y no sustituyen diagnóstico médico.
      </p>
    </div>

    <form v-if="!formSubmitted" @submit.prevent="checkForm" class="mb-4">
      <!-- Datos Personales -->
      <div class="form-section">
        <h2 class="section-title">Datos Personales*</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Sexo*" required />
            <Dropdown v-model="sexo" :options="genderOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="sexoError">{{ sexoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Grupo de edad*" required />
            <Dropdown v-model="grupo_edad" :options="ageOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="grupo_edadError">{{ grupo_edadError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Grupo racial o étnico*" required />
            <Dropdown v-model="grupo_racial" :options="raceOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="grupo_racialError">{{ grupo_racialError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Nivel educativo*" required />
            <Dropdown v-model="nivel_educativo" :options="educationOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="nivel_educativoError">{{ nivel_educativoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Nivel de ingresos*" required />
            <Dropdown v-model="ingresos_grupo" :options="incomeOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="ingresos_grupoError">{{ ingresos_grupoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="País*" required />
            <Dropdown v-model="pais" :options="countryOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" showClear filter class="w-full">
              <template #option="slotProps">
                <div class="flex items-center gap-2">
                  <span :class="'fi fi-' + slotProps.option.code?.toLowerCase()"></span>
                  <span>{{ slotProps.option.label }}</span>
                </div>
              </template>
              <template #value="slotProps">
                <div v-if="slotProps.value" class="flex items-center gap-2">
                  <span
                    :class="'fi fi-' + countryOptions.find(c => c.value === slotProps.value)?.code?.toLowerCase()"></span>
                  <span>{{countryOptions.find(c => c.value === slotProps.value)?.label}}</span>
                </div>
                <span v-else class="p-dropdown-empty">Seleccione su país</span>
              </template>
            </Dropdown>
            <small class="error-message" v-if="paisError">{{ paisError }}</small>
          </div>
        </div>
      </div>

      <!-- Biométricas -->
      <div class="form-section">
        <h2 class="section-title">Medidas Biométricas*</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Altura (cm)*" tooltip="Ingrese su altura en centímetros. Ej.: 175" required />
            <InputNumber v-model="altura" mode="decimal" :min="100" :max="250" class="w-full" />
            <small class="error-message" v-if="alturaError">{{ alturaError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Peso (kg)*" tooltip="Ingrese su peso en kilogramos. Ej.: 70" required />
            <InputNumber v-model="peso" mode="decimal" :min="30" :max="300" class="w-full" />
            <small class="error-message" v-if="pesoError">{{ pesoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Índice de Masa Corporal (IMC)*"
              tooltip="El IMC relaciona peso y altura. Un valor alto indica mayor riesgo de diabetes." />
            <InputNumber :modelValue="bmi" disabled class="w-full" :minFractionDigits="2" :maxFractionDigits="2" />
          </div>
        </div>
      </div>

      <!-- Historial Médico -->
      <div class="form-section">
        <h2 class="section-title">Historial Médico*</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Hipertensión arterial*" tooltip="¿Tiene hipertensión arterial diagnosticada?" required />
            <Dropdown v-model="presion_alta" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="presion_altaError">{{ presion_altaError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Colesterol elevado*" tooltip="¿Tiene colesterol elevado diagnosticado?" required />
            <Dropdown v-model="colesterol_alto" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="colesterol_altoError">{{ colesterol_altoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Antecedentes de ACV*" tooltip="¿Ha tenido un accidente cerebrovascular?" required />
            <Dropdown v-model="historial_acv" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="historial_acvError">{{ historial_acvError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Enfermedad cardíaca*" tooltip="¿Tiene enfermedades del corazón?" required />
            <Dropdown v-model="historial_cardiaco" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="historial_cardiacoError">{{ historial_cardiacoError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Dificultad para caminar*" tooltip="¿Tiene dificultad para caminar o subir escaleras?"
              required />
            <Dropdown v-model="dificultad_caminar" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="dificultad_caminarError">{{ dificultad_caminarError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Fumador (100+ cigarrillos)*" tooltip="¿Ha fumado más de 100 cigarrillos en su vida?"
              required />
            <Dropdown v-model="fumo_100_cigs" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="fumo_100_cigsError">{{ fumo_100_cigsError }}</small>
          </div>
        </div>
      </div>

      <!-- Hábitos -->
      <div class="form-section">
        <h2 class="section-title">Hábitos y Estilo de Vida*</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Actividad física habitual*" tooltip="¿Hace ejercicio regularmente?" required />
            <Dropdown v-model="actividad_fisica" :options="activityOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="actividad_fisicaError">{{ actividad_fisicaError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Ejercicio ≥300 min/semana*" tooltip="¿Hace al menos 300 min de ejercicio semanal?"
              required />
            <Dropdown v-model="actividad_300_min" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="actividad_300_minError">{{ actividad_300_minError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Fortalecimiento muscular*" tooltip="¿Hace ejercicios de fuerza 2+ veces por semana?"
              required />
            <Dropdown v-model="actividad_muscular" :options="yesNoOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="actividad_muscularError">{{ actividad_muscularError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Consumo de frutas*" tooltip="¿Cuántas veces come frutas por semana?" required />
            <Dropdown v-model="frecuencia_frutas" :options="frequencyOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="frecuencia_frutasError">{{ frecuencia_frutasError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Consumo de verduras*" tooltip="¿Cuántas veces come verduras por semana?" required />
            <Dropdown v-model="frecuencia_verduras" :options="frequencyOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="frecuencia_verdurasError">{{ frecuencia_verdurasError }}</small>
          </div>
        </div>
      </div>

      <!-- Salud -->
      <div class="form-section">
        <h2 class="section-title">Estado de Salud Percibida*</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Salud general*" tooltip="¿Cómo evalúa su salud en general?" required />
            <Dropdown v-model="salud_general" :options="healthOptions" optionLabel="label" optionValue="value"
              placeholder="Seleccione" class="w-full" />
            <small class="error-message" v-if="salud_generalError">{{ salud_generalError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Días con mala salud física*"
              tooltip="¿Cuántos días tuvo malestar físico en el último mes?" required />
            <InputNumber v-model="dias_mala_salud_fisica" :min="0" :max="30" class="w-full" />
            <small class="error-message" v-if="dias_mala_salud_fisicaError">{{ dias_mala_salud_fisicaError }}</small>
          </div>
          <div class="field">
            <InfoLabel label="Días con mala salud mental*"
              tooltip="¿Cuántos días tuvo malestar mental en el último mes?" required />
            <InputNumber v-model="dias_mala_salud_mental" :min="0" :max="30" class="w-full" />
            <small class="error-message" v-if="dias_mala_salud_mentalError">{{ dias_mala_salud_mentalError }}</small>
          </div>
        </div>
      </div>

      <div class="text-center">
        <Button label="Enviar Datos" class="submit-button" type="submit" :loading="loading" :disabled="loading" />
      </div>
    </form>

    <!-- Bloque de predicción debajo del formulario -->
    <div v-if="formSubmitted && prediction !== null" class="prediction-message">
      <div :class="{
        'prediction-positive': prediction === 1,
        'prediction-negative': prediction === 0
      }" class="prediction-box">
        <h2 class="prediction-title">
          {{ prediction === 1 ? '¡Atención!' : '¡Felicidades!' }}
        </h2>
        <p class="prediction-text">
          <span v-if="prediction === 1">
            Nuestro modelo indica que <b>podría tener riesgo de desarrollar Diabetes Tipo 2</b>.
            Este resultado es orientativo y no sustituye diagnóstico médico.
          </span>
          <span v-else>
            Nuestro modelo indica que <b>no presenta riesgo elevado de desarrollar Diabetes Tipo 2</b>.
            No obstante, mantenga hábitos saludables y realice chequeos periódicos para su bienestar.
          </span>
        </p>

        <p class="mt-4 mb-4 text-sm text-gray-700">
          <span v-if="prediction === 1">
            Le invitamos a consultar las métricas y gráficos interactivos en la sección de métricas de diabetes. Allí
            podrá
            entender mejor los factores y hábitos que influyen en el desarrollo de esta enfermedad, y conocer
            recomendaciones para reducir su riesgo y llevar una vida más saludable.
          </span>
          <span v-else>
            También puede revisar las métricas y gráficos interactivos disponibles en la sección de métricas de diabetes
            para reforzar sus buenos hábitos y conocer áreas clave para mantener su salud y prevenir la aparición de
            diabetes en el futuro.
          </span>
        </p>

        <router-link to="/metricas-diabetes">
          <Button label="Consultar métricas" class="mt-5 w-full md:w-auto" />
        </router-link>
      </div>
    </div>

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

.section-title {
  color: var(--primary-color);
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.error-message {
  color: #dc2626;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.submit-button {
  width: auto;
  margin-top: 1.5rem;
  padding: 1rem 3rem;
}

[required] label:after {
  content: " *";
  color: #dc2626;
}

.p-dropdown {
  width: 100%;
}

.prediction-box {
  max-width: 800px;
  margin: 1.5rem auto;
  padding: 2rem;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.prediction-positive {
  background-color: #fee2e2;
  color: #b91c1c;
}

.prediction-negative {
  background-color: #dcfce7;
  color: #166534;
}

.prediction-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.prediction-text {
  font-size: 1.1rem;
  line-height: 1.6;
}
</style>