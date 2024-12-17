<template>
    
    <div>
        <h1>Registered user are </h1>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Email ID</th>
                    <th>Active</th>
                    <th>Username</th>
                    <th>Service Type</th>
                    <th>Experience</th>
                    <th>Pincode</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr v-for="(user,index) in allUsers" :key="index">
                    <td>{{ user.id }}</td>
                    <td>{{ user.email }}</td>
                    <td><button v-if="!user.active" @click="approve(user.id)">Approve</button>
                        <button v-else @click="deapprove(user.id)">Deactivate</button>
                    </td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.name }}</td>
                    <td>{{ user.service_name }}</td>
                    <td>{{ user.experience }}</td>
                    <td>{{ user.pincode }}</td>
                    <td><button v-if="!user.flag" @click="flag(user.id)">Flagged!</button>
                        <button v-else @click="deflag(user.id)">Not Flagged!</button>
                    </td>


                </tr>
            </tbody>

        </table>
    </div>


</template>
<script>
export default{
    data(){
        return {
            allUsers:[],
            token : localStorage.getItem("auth-token")
        }
    },

    methods:{
        //method to approve user
       async approve(id){
        const res = await fetch(`/activate/sponser_or_influncer/${id}`,{
            headers:{
                'Authentication-Token':this.token,
            }
        }) //fetching url with sponser id
        const data = await res.json()
        if (res.ok){
            alert(data.message)
        }
        else{
            alert(data.message)
        }
        
       },


       // method to deapprove user
       async deapprove(id){

        const res= await fetch(`/deactivate/${id}`,{
            headers:{
                'Authentication-Token':this.token,
            }
        });


        const data = await res.json();

        if(res.ok){
            alert(data.message)
        }
        else{
        alert(data.message)
        }
       },

       // method to flag user

       async flag(id){
        const res = await fetch('/flagged-user',{
            headers:{
                'Authentication-Token':this.token,
            }

        });

        const data = await res.json();
        if (res.ok){
            alert(data.message)
        }
        else{
            alert(data.message)
        }
       },


       // method to deflag user
       async deflag(id){
        const res = await fetch('/deflag-user',{
            headers:{
                'Authentication-Token':this.token,
            }

        });

        const data = await res.json();
        if (res.ok){
            alert(data.message)
        }
        else{
            alert(data.message)
        }
       }


    },

    async mounted(){

        const res = await fetch('/users',{
            headers:{
                'Authentication-Token':this.token,
            },
        }) 

        const data = await res.json()
        if (res.ok){
            this.allUsers = data
        }

    }

}
</script>

