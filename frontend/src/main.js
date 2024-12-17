import { createApp } from 'vue'

import App from './App.vue';
import Navbar from './components/Navbar.vue';
import router from './router.js'


//navigating to login page if user is somewhere else without login 

// router.beforeEach((to,from,next)=> {
//     if (to.name !== 'Login' && !localStorage.getItem('auth-token')? true : false)
//         next({name:'Login'})
//     else next()
// })

const app = createApp(App);

app.component('nav-bar',Navbar)


app.use(router)

app.mount('#app');