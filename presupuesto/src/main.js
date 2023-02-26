import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import { BootstrapVue } from 'bootstrap-vue'
import './app.scss'

Vue.use(BootstrapVue)

createApp(App).use(store).mount('#app')
