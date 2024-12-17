<template>
    <div>
        <router-link to ='/login' v-show="!is_login">Login</router-link> | 
        <router-link to ='/registration' v-show="!is_login">Register</router-link>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Project</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        <!-- option for admin -->
        </li>
        <router-link to='/user' v-if="role=='admin'"><li class="nav-item" >
          <span class="nav-link">User</span>
        </li></router-link>




        <!-- option for sponser -->


      
        <router-link to='/create-campaign' v-if="role=='sponser'"><li class="nav-item" >
          <span class="nav-link">Add  New Campaign</span>
        </li></router-link>

        <router-link to='/all-campaign' v-if="['sponser','admin'].includes(role)"><li class="nav-item" >
          <span class="nav-link">All Campaign</span>
        </li></router-link>




        <li class="nav-item" v-if="is_login">
        <button @click="logout">
        <span>Logout</span></button>
        </li>

      </ul>
    </div>
  </div>
</nav>
    </div>
</template>

<script>
export default{
  data(){
    return {
      role: localStorage.getItem('role'),
      is_login : localStorage.getItem('auth-token')
    }
  },

methods:{
  logout(){
    localStorage.removeItem('auth-token')
    localStorage.removeItem('role')
    this.$router.push({path:'/login'})
  }

}
}

</script>