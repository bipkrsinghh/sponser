<template>
    <div class = 'd-flex justify-content-center align-items-center flex-column ' style="margin-top: 30vh">
    <div class="mb-3 p-2 h1">Registration Form</div>
    <div class="text-danger">{{ error }}</div>
    <div class="mb-3 p-2 bg-green">
      <label for="user_email" class="form-label">Email address</label>
      <input v-model = 'cred.email' type="email" class="form-control " id="user_email" placeholder="name@example.com">
    </div>
    <div class="mb-3 p-2">
      <label for="user_name" class="form-label">Username</label>
      <input v-model="cred.username" type="text" class="form-control" id="user_name" placeholder="Username">
    </div>
    <div class="mb-3 p-2">
      <label for="name" class="form-label">Name</label>
      <input v-model="cred.name" type="text" class="form-control" id="name" placeholder="Enter your name here">
    </div>

  <!-- now asking for role   collecting roles -->
   <div class="mb-3 p-2"> <b>Want to register as a</b></div>
   <div class="form-check form-check-inline mb-3 p-2">
    <input v-model='cred.role' class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" value="sponser">
    <label class="form-check-label" for="flexRadioDefault1">
      Sponser
    </label>
  </div>
  <div class="form-check form-check-inline mb-3 p-2 ">
    <input v-model='cred.role' class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value ="influncer">
    <label class="form-check-label" for="flexRadioDefault2">
      Influncer
    </label>
  </div>

  <div v-if="cred.role=== 'sponser'">
    <div class="mb-3 p-2">
        <label for="user_company" class="form-label">Company Name</label>
        <input v-model="cred.company_name" type="text" class="form-control" id="user_company" placeholder="Enter company name">
    </div>
    <div class="mb-3 p-2">
        <label for="user_industry" class="form-label">Industry Type</label>
        <input v-model="cred.industry_type" type="text" class="form-control" id="user_industry" placeholder="Enter type of Industries">
    </div>
  </div>

<div v-if="cred.role=== 'influncer'">
    <div class="mb-3 p-2">
        <label for="category" class="form-label">Category</label>
        <input v-model="cred.category" type="text" class="form-control" id="category" placeholder="Enter your Category here">
    </div>

    <div class="mb-3 p-2">
        <label for="niche" class="form-label">Niche</label>
        <input v-model="cred.niche" type="text" class="form-control" id="niche" placeholder="Enter your Niche here">
    </div>

    <div class="mb-3 p-2">
        <label for="reach" class="form-label">Reach</label>
        <input v-model="cred.reach" type="text" class="form-control" id="reach" placeholder="Enter Number of Followers">
    </div>
</div>
  <div class="mb-3 p-2">
      <label for="user_password" class="form-label">Password</label>
      <input v-model="cred.password" type="text" class="form-control" id="user_name" placeholder="Enter your password">
    </div> 
    
  <div class="p-2">
      <button class="btn btn-primary mt2" @click="register">Register</button>
  </div>
</div>
</template>

<script>
  export default{
    data(){
        return{
            cred:{
                'email': null,
                'username':null,
                'name': null,
                'role': null,
                'company_name':null,
                'industry_type':null,
                'category':null,
                'niche':null,
                'reach':null,
                'password':null,
            },
            error:null,
        }
    },
    methods:{
        async register(){
            const res = await fetch('/user-register',{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json',
                },
                body :JSON.stringify(this.cred),
            })
            
            const data = await res.json();
            if(res.ok){

                this.$router.push('/login')
            }
            else{
                this.error = data.message
            }
        }
    }
  }

</script>