import { createRouter, createWebHistory } from 'vue-router'

import Home from './components/Home.vue'
import Login from './components/Login.vue'
//import Navbar from './components/Navbar.vue'
import Register from './components/Registration.vue'
import User from './components/User.vue'
import CampaignForm from './components/CampaignForm.vue'
import AdForm from './components/AdForm.vue'
import Campaign from './components/Campaign.vue'



const routes = [
    {path:'/',component:Home},
    {path:'/login',component:Login},
    {path:'/registration',component: Register},
    {path:'/user',component:User},
    {path:'/create-campaign',component:CampaignForm},
    {path:'/create-ad/:campaignId',name:'CreateAd',component:AdForm},
    {path:'/all-campaign',component:Campaign}

]


const router = createRouter({
    history : createWebHistory(),
    routes
})


export default router

