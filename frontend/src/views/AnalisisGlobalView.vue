<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import * as echarts from 'echarts'

const chartMapRef = ref<HTMLDivElement | null>(null)
const chartTimeRef = ref<HTMLDivElement | null>(null)
const chartMapInstance = ref<any>(null)
const chartTimeInstance = ref<any>(null)

const selectedContinent = ref<string>('Todos')
const selectedYear = ref<string>('Todos')

const availableContinents = ref<string[]>([])
const availableYears = ref<string[]>([])

let timeDataRaw: any[] = []

async function loadFiltersFromTimeData() {
  try {
    const res = await fetch('http://localhost:8000/api/promedio-diabetes-tiempo/')
    if (!res.ok) throw new Error('No se pudo obtener datos para filtros')
    timeDataRaw = await res.json()

    const años = Array.from(new Set(timeDataRaw.map(item => item.anio))).sort()
    const continentes = Array.from(new Set(timeDataRaw.map(item => item.continente))).sort()

    availableYears.value = ['Todos', ...años.map(String)]
    availableContinents.value = ['Todos', ...continentes]
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  try {
    const worldResponse = await fetch('/maps/world.json')
    if (!worldResponse.ok) throw new Error('No se pudo cargar el GeoJSON')
    const worldGeoJson = await worldResponse.json()
    echarts.registerMap('world', worldGeoJson)

    await loadFiltersFromTimeData()

    chartMapInstance.value = echarts.init(chartMapRef.value!)
    chartTimeInstance.value = echarts.init(chartTimeRef.value!)

    chartMapInstance.value.setOption(getMapOption([]))
    chartTimeInstance.value.setOption(getTimeOption([]))

    await loadMapData()
    await loadTimeData()
  } catch (error) {
    console.error(error)
  }
})

watch([selectedContinent, selectedYear], async () => {
  await loadMapData()
  await loadTimeData()
})

async function loadMapData() {
  try {
    let url = 'http://localhost:8000/api/promedio-diabetes-por-pais/'
    const params = new URLSearchParams()

    if ([...params].length > 0) {
      url += `?${params.toString()}`
    }

    const res = await fetch(url)
    if (!res.ok) throw new Error('Error al obtener datos del mapa')
    const dataJson = await res.json()

    const mappedData = (dataJson || []).map((item: any) => ({
      name: item.pais,
      value: Number((item.promedio_diabetes_bin * 100).toFixed(2))
    }))

    chartMapInstance.value.setOption({
      series: [
        {
          data: mappedData
        }
      ]
    })
  } catch (error) {
    console.error(error)
  }
}

async function loadTimeData() {
  try {
    let url = 'http://localhost:8000/api/promedio-diabetes-tiempo/'
    const params = new URLSearchParams()

    if (selectedContinent.value !== 'Todos') {
      params.append('continente', selectedContinent.value)
    }
    if (selectedYear.value !== 'Todos') {
      params.append('anio', selectedYear.value)
    }
    if ([...params].length > 0) {
      url += `?${params.toString()}`
    }

    const res = await fetch(url)
    if (!res.ok) throw new Error('Error al obtener datos temporales')
    const dataJson = await res.json()

    const sortedData = dataJson.sort(
      (a: any, b: any) => a.anio * 100 + a.mes - (b.anio * 100 + b.mes)
    )

    const labels = sortedData.map(
      (item: any) => `${item.anio}-${String(item.mes).padStart(2, '0')}`
    )
    const values = sortedData.map((item: any) =>
      Number((item.promedio_diabetes_bin * 100).toFixed(2))
    )

    chartTimeInstance.value.setOption({
      xAxis: {
        data: labels,
        axisLabel: {
          rotate: 45
        }
      },
      series: [
        {
          data: values
        }
      ]
    })
  } catch (error) {
    console.error(error)
  }
}

function getMapOption(initialData: any[]) {
  const toolboxFeatures: Record<string, any> = {
    allContinents: {
      show: true,
      title: 'Todos Continentes',
      icon: 'rect',
      onclick: () => {
        selectedContinent.value = 'Todos'
      }
    }
  }
  for (const cont of availableContinents.value.filter(c => c !== 'Todos')) {
    toolboxFeatures[`continent_${cont}`] = {
      show: true,
      title: cont,
      icon: 'rect',
      onclick: () => {
        selectedContinent.value = cont
      }
    }
  }

  return {
    title: {
      text: 'Promedio de Diabetes por País (Usuarios)',
      left: 'center',
      top: 10,
      textStyle: {
        fontSize: 16,
        color: '#2e7d32'
      }
    },
    tooltip: {
      trigger: 'item',
      formatter: (params: any) => `${params.name}<br/>${params.value || 0}%`
    },
    toolbox: {
      show: true,
      orient: 'vertical',
      left: 'left',
      top: 'center',
      feature: toolboxFeatures
    },
    visualMap: {
      min: 0,
      max: 100,
      text: ['Alto %', 'Bajo %'],
      calculable: true,
      inRange: {
        color: ['#004d00', '#99ff99', '#ffcccc', '#990000']
      },
      left: 'left',
      top: 'middle',
      orient: 'vertical',
      itemWidth: 20,
      itemHeight: 120,
      textGap: 10,
      textStyle: {
        fontSize: 12
      }
    },
    media: [
      {
        query: {
          maxWidth: 480
        },
        option: {
          visualMap: {
            itemWidth: 12,
            itemHeight: 80,
            textGap: 5,
            textStyle: {
              fontSize: 10
            },
            left: 'left',
            top: 'center'
          }
        }
      }
    ],
    series: [
      {
        name: 'Diabetes',
        type: 'map',
        map: 'world',
        roam: true,
        emphasis: {
          itemStyle: {
            areaColor: '#a3cfff'
          }
        },
        data: initialData
      }
    ]
  }
}

function getTimeOption(initialData: any[]) {
  return {
    title: {
      text: 'Promedio de Diabetes por Mes y Año',
      left: 'center',
      top: 10,
      textStyle: {
        fontSize: 16,
        color: '#2e7d32'
      }
    },
    tooltip: {
      trigger: 'axis',
      formatter: (params: any) => {
        const p = params[0]
        return `${p.axisValue}<br/>Promedio Diabetes: ${p.data}%`
      }
    },
    xAxis: {
      type: 'category',
      data: [],
      axisLabel: {
        rotate: 45,
        interval: 0
      },
      axisTick: {
        alignWithLabel: true
      },
      boundaryGap: false
    },
    yAxis: {
      type: 'value',
      min: 0,
      max: 100,
      axisLabel: {
        formatter: '{value} %'
      },
      splitLine: {
        show: true
      }
    },
    series: [
      {
        data: initialData,
        type: 'line',
        smooth: true,
        name: 'Promedio Diabetes (%)',
        lineStyle: { width: 3 },
        itemStyle: { color: '#5470C6' }
      }
    ],
    grid: { bottom: '20%', left: '12%', right: '10%', top: '20%' }
  }
}
</script>

<template>
  <div class="mb-6">
    <div class="my-6 text-center">
      <h1 class="text-3xl font-bold text-green-600">
        Análisis Global de Predicciones
      </h1>
    </div>
    <p class="text-base text-color-secondary mb-4 px-4">
      Este panel muestra el promedio del riesgo de diabetes predicho para cada país, calculado
      a partir de los datos ingresados por usuarios en nuestro formulario. También puedes explorar
      cómo estos valores han evolucionado en el tiempo por continente y año.
      <strong class="text-red-600">
        Todos los datos reflejan únicamente predicciones basadas en encuestas de esta aplicación.
      </strong>
    </p>
  </div>

  <div class="form-section">
    <div ref="chartMapRef" class="chart-map"></div>
  </div>

  <div class="form-section">
    <div class="filters">
      <div class="filter-group">
        <label>Continente:</label>
        <div class="button-group continent-group">
          <button
            v-for="cont in availableContinents"
            :key="cont"
            :class="['btn-continent', { selected: selectedContinent === cont }]"
            @click="selectedContinent = cont"
            type="button"
          >
            {{ cont }}
          </button>
        </div>
      </div>

      <div class="filter-group">
        <label>Año:</label>
        <div class="button-group year-group">
          <button
            v-for="year in availableYears"
            :key="year"
            :class="['btn-year', { selected: selectedYear === year }]"
            @click="selectedYear = year"
            type="button"
          >
            {{ year }}
          </button>
        </div>
      </div>
    </div>

    <div ref="chartTimeRef" class="chart-time"></div>
  </div>
</template>

<style scoped>
.form-section {
  margin: 0.3rem 0.5rem;
  background: #f9f9f9;
  padding: 1rem;
  border-radius: 8px;
  width: 100%;
  box-sizing: border-box;
}

.filters {
  margin-bottom: 0.7rem;
  display: flex;
  gap: 1rem;
  flex-wrap: nowrap;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.filter-group {
  display: flex;
  flex-direction: column;
  min-width: 120px;
  flex: 0 0 auto;
}

.filter-group > label {
  font-weight: 600;
  margin-bottom: 0.4rem;
}

.button-group {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.5rem;
  align-items: center;
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.btn-continent,
.btn-year {
  flex: 0 0 auto;
  min-width: 60px;
  min-height: 36px;
  padding: 0.4rem 1rem;
  font-size: 0.9rem;
  white-space: nowrap;
  user-select: none;
  border-radius: 5px;
  cursor: pointer;
  border: 1.5px solid #ccc;
  background-color: white;
  font-weight: 500;
  transition: all 0.2s ease;
}

.btn-continent {
  color: #2e7d32;
}
.btn-continent:hover {
  border-color: #388e3c;
  background-color: #c8e6c9;
}
.btn-continent.selected {
  background-color: #2e7d32;
  color: white;
  border-color: #2e7d32;
}

.btn-year {
  color: #1565c0;
}
.btn-year:hover {
  border-color: #1976d2;
  background-color: #bbdefb;
}
.btn-year.selected {
  background-color: #1565c0;
  color: white;
  border-color: #1565c0;
}

.chart-map {
  width: 100%;
  height: 600px;
  margin-top: 0;
}

.chart-time {
  width: 100%;
  height: 400px;
  margin-top: 0.5rem;
}

@media (max-width: 480px) {
  .filters {
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  .filter-group {
    min-width: 100%;
    flex: none;
  }
  .chart-map {
    height: 350px;
  }
  .chart-time {
    height: 300px;
  }
  .btn-continent,
  .btn-year {
    min-width: 50px;
    min-height: 30px;
    padding: 0.3rem 0.8rem;
    font-size: 0.8rem;
  }
}
</style>
