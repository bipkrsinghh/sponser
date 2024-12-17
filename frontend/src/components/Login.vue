<template>


  <!-- Email input -->
  <div data-mdb-input-init class="form-outline mb-4">
    <input v-model="cred.email" type="email" id="form2Example1" class="form-control" />
    <label class="form-label" for="form2Example1">Email address</label>
  </div>

  <!-- Password input -->
  <div data-mdb-input-init class="form-outline mb-4">
    <input v-model="cred.password" type="password" id="form2Example2" class="form-control" />
    <label class="form-label" for="form2Example2">Password</label>
  </div>

  <!-- 2 column grid layout for inline styling -->
  <div class="row mb-4">
    <div class="col d-flex justify-content-center">
      <!-- Checkbox -->
      <div class="form-check">
        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
        <label class="form-check-label" for="form2Example31"> Remember me </label>
      </div>
    </div>

    <div class="col">
      <!-- Simple link -->
      <a href="#!">Forgot password?</a>
    </div>
  </div>

  <!-- Submit button -->
  <button @click="login" type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4">Sign in</button>

  <!-- Register buttons -->
  <div class="text-center">
    <p>Not a member? <a href="#!">Register</a></p>
    <p>or sign up with:</p>
    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-facebook-f"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-google"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-twitter"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-github"></i>
    </button>
  </div>
   
<!-- <div class="text-danger">{{ error }}</div>    
<div class = 'd-flex justify-content-center' style="margin-top: 30vh">
    <div class="mb-3 p-5 bg-light">
    <label for="user_email" class="form-label">Email address</label>
    <input v-model = 'cred.email' type="email" class="form-control" id="user_email" placeholder="name@example.com">
    </div>
    <div class="mb-3">
    <label for="user_password" class="form-label">Password</label>
    <input v-model='cred.password' type="password" class="form-control" id="user_password" placeholder="password">
    <button class="btn btn-primary mt2" @click="login">Login</button>
</div>
</div> -->
</template>

<script>
export default{
    data(){
        return{
            cred :{
                "email" : null,
                "password":null
            },
            error:null,
            

        }
    },
    methods:{
        async login(){
            
                const res = await fetch('/user-login',{
                    method: 'POST',
                    headers : {
                        'Content-Type' : 'application/json',
                    },
                    body: JSON.stringify(this.cred),
                });

                // in case if the data i got is not valid
                const data = await res.json();
                if(res.ok){
                // after that now store the token in local variable that will be useful to direct the user to respective dashboard
                localStorage.setItem('auth-token',data.token)
                //passing role information to home.vue so that it can be used to rendered component based on role info
                //now storing role information in local storage too
                localStorage.setItem('role',data.role)    
                this.$router.push({ path:'/', query : {role:data.role}})
                }
            else {
                this.error = data.message
        }
    }
    }
}

</script>


