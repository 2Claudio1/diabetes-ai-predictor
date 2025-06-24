<template>
  <div class="diabetes-test-container">
    <div>aaaa</div>
    <Card>
      <div>bbbb</div>
      <template #title>
        Test de Riesgo de Diabetes
      </template>
      <template #subtitle>
        Complete todas las secciones para obtener una evaluación precisa
      </template>

      <TabView>
          <!-- Sección 1: Datos Personales -->
          <TabPanel header="Datos Personales">
            <div class="p-fluid grid">
              <div class="field col-12 md:col-6">
                <label for="age">Edad</label>
                <Dropdown
                  id="age"
                  v-model="form.grupo_edad"
                  :options="ageGroups"
                  optionLabel="label"
                  optionValue="value"
                  placeholder="Seleccione su rango de edad"
                />
              </div>
            </div>
          </TabPanel>
      </TabView>

      <form @submit.prevent="submitForm">
        <TabView>
          <!-- Sección 1: Datos Personales -->
          <TabPanel header="Datos Personales">
            <div class="p-fluid grid">
              <div class="field col-12 md:col-6">
                <label for="age">Edad</label>
                <Dropdown
                  id="age"
                  v-model="form.grupo_edad"
                  :options="ageGroups"
                  optionLabel="label"
                  optionValue="value"
                  placeholder="Seleccione su rango de edad"
                />
              </div>

              <div class="field col-12 md:col-6">
                <label>Sexo</label>
                <div class="flex gap-3">
                  <RadioButton
                    v-model="form.sexo"
                    inputId="sexo_m"
                    name="sexo"
                    :value="1"
                  />
                  <label for="sexo_m">Masculino</label>
                  <RadioButton
                    v-model="form.sexo"
                    inputId="sexo_f"
                    name="sexo"
                    :value="2"
                  />
                  <label for="sexo_f">Femenino</label>
                </div>
              </div>

              <div class="field col-12 md:col-6">
                <label for="weight">Peso (kg)</label>
                <InputNumber
                  id="weight"
                  v-model="weight"
                  suffix=" kg"
                  :min="30"
                  :max="200"
                />
              </div>

              <div class="field col-12 md:col-6">
                <label for="height">Altura (cm)</label>
                <InputNumber
                  id="height"
                  v-model="height"
                  suffix=" cm"
                  :min="100"
                  :max="250"
                />
              </div>

              <div class="field col-12">
                <label>BMI: {{ bmi.toFixed(2) }}</label>
                <ProgressBar :value="bmiProgress" :showValue="false"></ProgressBar>
              </div>
            </div>
          </TabPanel>

          <!-- Sección 2: Historial Clínico -->
          <TabPanel header="Historial Clínico">
            <div class="p-fluid grid">
              <div class="field col-12 md:col-6">
                <label>¿Tiene presión arterial alta?</label>
                <SelectButton
                  v-model="form.presion_alta"
                  :options="yesNoOptions"
                  optionLabel="label"
                  optionValue="value"
                />
              </div>

              <div class="field col-12 md:col-6">
                <label>¿Colesterol alto?</label>
                <SelectButton
                  v-model="form.colesterol_alto"
                  :options="yesNoOptions"
                  optionLabel="label"
                  optionValue="value"
                />
              </div>
            </div>
          </TabPanel>

          <!-- Sección 3: Estilo de Vida -->
          <TabPanel header="Estilo de Vida">
            <div class="p-fluid grid">
              <div class="field col-12">
                <label>¿Realiza actividad física regular?</label>
                <SelectButton
                  v-model="form.actividad_fisica"
                  :options="activityOptions"
                  optionLabel="label"
                  optionValue="value"
                />
              </div>
            </div>
          </TabPanel>
        </TabView>

        <div class="flex justify-content-end mt-5">
          <Button 
            type="submit" 
            label="Evaluar Riesgo" 
            icon="pi pi-check" 
          />
        </div>
      </form>
    </Card>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Card from 'primevue/card'
import TabView from 'primevue/tabview'
import TabPanel from 'primevue/tabpanel'
import Dropdown from 'primevue/dropdown'
import InputNumber from 'primevue/inputnumber'
import RadioButton from 'primevue/radiobutton'
import SelectButton from 'primevue/selectbutton'
import Button from 'primevue/button'
import ProgressBar from 'primevue/progressbar'

// Opciones para los dropdowns/selects
const ageGroups = ref([
  { label: '18-24 años', value: 1 },
  { label: '25-29 años', value: 2 },
  { label: '30-34 años', value: 3 },
  { label: '35-39 años', value: 4 },
  { label: '40-44 años', value: 5 },
  { label: '45-49 años', value: 6 },
  { label: '50-54 años', value: 7 },
  { label: '55-59 años', value: 8 },
  { label: '60-64 años', value: 9 },
  { label: '65-69 años', value: 10 },
  { label: '70-74 años', value: 11 },
  { label: '75-79 años', value: 12 },
  { label: '80+ años', value: 13 }
])

const yesNoOptions = ref([
  { label: 'Sí', value: 1 },
  { label: 'No', value: 0 }
])

const activityOptions = ref([
  { label: 'Sedentario', value: 1 },
  { label: 'Moderado', value: 2 },
  { label: 'Activo', value: 3 }
])

// Datos del formulario
const form = ref({
  grupo_edad: null,
  sexo: null,
  presion_alta: null,
  colesterol_alto: null,
  actividad_fisica: null
})

// Cálculo de BMI
const weight = ref(70)
const height = ref(170)
const bmi = computed(() => {
  return weight.value / ((height.value / 100) ** 2)
})
const bmiProgress = computed(() => {
  return Math.min(bmi.value * 2, 100)
})

const submitForm = () => {
  console.log('Formulario enviado:', form.value)
}
</script>

<style scoped>
.diabetes-test-container {
  max-width: 900px;
  margin: 2rem auto;
}

:deep(.p-tabview-nav) {
  justify-content: center;
}

:deep(.p-tabview-panels) {
  padding: 1.5rem 0;
}
</style>