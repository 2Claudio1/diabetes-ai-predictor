<script setup lang="ts">
import { ref } from 'vue';
import { useForm } from "vee-validate";
import Dropdown from 'primevue/dropdown';
import InputNumber from 'primevue/inputnumber';
import Button from 'primevue/button';
import Tooltip from 'primevue/tooltip';
import InfoLabel from '@/components/shared/InfoLabel.vue';

// Registrar directiva localmente
const vTooltip = Tooltip;

const { handleSubmit } = useForm();

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

// Calcular BMI
const calcularBMI = () => {
  if (form.value.altura && form.value.peso) {
    const alturaMetros = (+form.value.altura) / 100;
    const peso = +form.value.peso;
    return (peso / (alturaMetros * alturaMetros)).toFixed(2);
  }
  return null;
};

// Opciones
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
  { label: 'Diariamente', value: 1 },
  { label: 'Frecuentemente', value: 2 },
  { label: 'Ocasionalmente', value: 3 },
  { label: 'Nunca', value: 4 }
];

const healthOptions = [
  { label: 'Mala', value: 1 },
  { label: 'Regular', value: 2 },
  { label: 'Buena', value: 3 },
  { label: 'Muy buena', value: 4 },
  { label: 'Excelente', value: 5 }
];

const checkForm = async () => {
  handleSubmit(async (values) => {
    console.log('Values:', values);
  })();
};
</script>

<template>
  <div class="form-container">
    <div class="mb-6">
      <div class="my-6 text-center">
        <h1 class="text-3xl font-bold text-primary">Predictor de Riesgo de Diabetes</h1>
      </div>
      <p class="text-xl text-color-secondary mt-2">
        Esta herramienta evalúa tu riesgo de diabetes tipo 2 basado en tus datos de salud y estilo de vida.
        <br>Los resultados son solo orientativos y no sustituyen diagnóstico médico.
      </p>
    </div>
    <form @submit.prevent="checkForm">
      <!-- Datos Personales -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Datos Personales</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Sexo" />
            <Dropdown v-model="form.sexo" :options="genderOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Grupo de edad" />
            <Dropdown v-model="form.grupo_edad" :options="ageOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Grupo racial / étnico" />
            <Dropdown v-model="form.grupo_racial" :options="raceOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Nivel educativo" />
            <Dropdown v-model="form.nivel_educativo" :options="educationOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Nivel de ingresos" />
            <Dropdown v-model="form.categoria_ingresos" :options="incomeOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
        </div>
      </div>

      <!-- Biométricas -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Medidas Biométricas</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Altura (cm)" tooltip="Ingrese su altura en centímetros. Ej.: 175" />
            <InputNumber v-model="form.altura" mode="decimal" :min="100" :max="250" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Peso (kg)" tooltip="Ingrese su peso en kilogramos. Ej.: 70" />
            <InputNumber v-model="form.peso" mode="decimal" :min="30" :max="300" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="IMC (BMI)" tooltip="El IMC relaciona peso y altura. Un valor alto indica mayor riesgo de diabetes." />
            <InputNumber :value="calcularBMI()" disabled class="w-full" />
          </div>
        </div>
      </div>

      <!-- Historial Médico -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Historial Médico</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Presión arterial alta" tooltip="¿Tiene presión alta diagnosticada?" />
            <Dropdown v-model="form.presion_alta" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Colesterol alto" tooltip="¿Tiene colesterol alto diagnosticado?" />
            <Dropdown v-model="form.colesterol_alto" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Historial de ACV" tooltip="¿Ha tenido un ACV?" />
            <Dropdown v-model="form.historial_acv" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Historial cardíaco" tooltip="¿Tiene enfermedades del corazón?" />
            <Dropdown v-model="form.historial_cardiaco" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Dificultad para caminar" tooltip="¿Tiene dificultad para caminar?" />
            <Dropdown v-model="form.dificultad_caminar" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Fumó más de 100 cigarrillos" tooltip="¿Ha fumado más de 100 cigarrillos en su vida?" />
            <Dropdown v-model="form.fumo_100_cigs" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
        </div>
      </div>

      <!-- Hábitos -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Hábitos y Estilo de Vida</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Nivel de actividad física" tooltip="¿Hace ejercicio regularmente?" />
            <Dropdown v-model="form.actividad_fisica" :options="activityOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="300+ min de actividad física semanal" tooltip="¿Hace al menos 300 min de ejercicio semanal?" />
            <Dropdown v-model="form.actividad_300min" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Fortalecimiento muscular" tooltip="¿Hace ejercicios de fuerza 2+ veces por semana?" />
            <Dropdown v-model="form.actividad_muscular" :options="yesNoOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Frecuencia de consumo de frutas" tooltip="¿Cuántas veces come frutas por semana?" />
            <Dropdown v-model="form.frecuencia_frutas" :options="frequencyOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Frecuencia de consumo de verduras" tooltip="¿Cuántas veces come verduras por semana?" />
            <Dropdown v-model="form.frecuencia_verduras" :options="frequencyOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
        </div>
      </div>

      <!-- Salud -->
      <div class="form-section">
        <h2 class="text-green-600 font-semibold text-xl mb-4">Estado de Salud</h2>
        <div class="grid">
          <div class="field">
            <InfoLabel label="Salud general autopercibida" tooltip="¿Cómo evalúa su salud en general?" />
            <Dropdown v-model="form.salud_general" :options="healthOptions" optionLabel="label" placeholder="Seleccione" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Días con mala salud física (último mes)" tooltip="¿Cuántos días tuvo malestar físico en el último mes?" />
            <InputNumber v-model="form.dias_mala_salud_fisica" :min="0" :max="30" class="w-full" />
          </div>
          <div class="field">
            <InfoLabel label="Días con mala salud mental (último mes)" tooltip="¿Cuántos días tuvo malestar mental en el último mes?" />
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
</style>
