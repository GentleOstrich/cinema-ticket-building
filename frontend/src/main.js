import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios"

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')
axios.defaults.baseURL = "http://127.0.0.1:8000/api"
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
