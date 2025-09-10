import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Tooltip from 'primevue/tooltip'
import 'primeicons/primeicons.css' // Para los íconos

import Aura from '@primevue/themes/aura';
import 'primeflex/primeflex.css';

import "flag-icons/css/flag-icons.min.css";

const app = createApp(App)

app.use(createPinia())
app.use(router)
//app.use(PrimeVue)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

// Registra la directiva globalmente
app.directive('tooltip', Tooltip)



app.mount('#app')
