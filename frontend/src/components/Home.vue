<template>
<nav-bar/>
<h1>hello from home template</h1>
<Admin v-if="userRole == 'admin'"/>
<Sponser v-if="userRole=='sponser'"/>
<Influncer v-if="userRole=='influncer'"/>
</template>


<script>
import Admin from './AdminDash.vue'
import Sponser from './SponserDash.vue'
import Influncer from './InfluncerDash.vue'

export default{
    data(){
        return{
            userRole : this.$route.query.role// getting this query from login.vue
        }
    },
    components :{
        Admin,
        Sponser,
        Influncer,
    }
}


</script>