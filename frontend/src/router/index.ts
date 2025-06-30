import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DiabetesTest from '@/views/DiabetesTestView.vue'
import Metrics from '@/views/MetricsView.vue'
import AnalisisGlobal from '@/views/AnalisisGlobalView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/teste-diabetes', component: DiabetesTest },
    { path: '/metricas-diabetes', component: Metrics },
    { path: '/analisis-global', component: AnalisisGlobal },
  ]
})

export default router
