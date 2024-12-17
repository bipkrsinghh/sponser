<template>
    <div>
        <input v-model="campaign.c_name" type="text" placeholder="Campaign Name"/>
        <input v-model="campaign.description" type="textarea" placeholder="Description"/>
        <input v-model="campaign.start_date" type="date" placeholder="Start date"/>
        <input v-model="campaign.end_date" type="date" placeholder="End date"/>
        <input v-model="campaign.c_budget" type="number" placeholder="Budget"/>
        <label>Visibility</label>
        <input  v-model="campaign.visibility" type="radio" id="yes" name="active" :value=True>
        <label for="yes">Private</label>
        <input v-model="campaign.visibility" type="radio" id="no" name="active" :value=False>
        <label for="no">Public</label>
        <button @click="createcampaign">Add Campaign</button>
        </div>
</template>

<script>
export default{
    data(){
        return{
            campaign:{
                'c_name':null,
                'description':null,
                'start_date':null,
                'end_date':null,
                'c_budget':null,
                'visibility':null,

            },
            
            token : localStorage.getItem('auth-token')

        }
    },
    methods:{
       async createcampaign(){
        const res = await fetch('/api/campaign_material',{
            method:'POST',
            headers:{
                'Authentication-Token': this.token,
                'Content-Type':'application/json',
            },
            
            body:JSON.stringify(this.campaign),
        }) //fetching url with sponser id
        
        
        const data = await res.json()
        
        if (res.ok){
            alert(data.message)
        }
        else{
            alert(data.message)
        }
        
       }
    },
}
</script>