<template>
        <div>
        <textarea v-model="ad.message"  placeholder="Ad Name"></textarea>
        <textarea v-model="ad.requirements" placeholder="Description"></textarea>
        <input v-model="ad.payment_amount" type="number" placeholder="Budget"/>
        <label for="campaign">Assign Campaign</label>
       
        
        <button @click="adCreation()">Add Ad</button>
        </div>
</template>

<script>
export default{
    props:['campaignId'],
    data(){
        return{
            ad:{
                'campaign_id':this.$route.params.campaignId,
                'influencer_id':null,
                'message':null,
                'requirements':null,
                'payment_amount':null,
                'status':'Pending',
            },
            //allCampaign:[],
            token:localStorage.getItem('auth-token')
        }
    },
    methods:{
        async adCreation(){
        const res = await fetch('/api/ad_material',{
            method:'POST',
            headers:{
                'Authentication-Token':this.token,
                'Content-Type':'application/json'
            },
            body: JSON.stringify(this.ad)
        }) //fetching url with sponser id
        const data = await res.json()
        
        console.log(this.ad.campaign_id)
        if (res.ok){
            alert(data.message)
        }
        else{
            alert(data.message)
        }
        
       }
    },



    async mounted(){
        const res = await fetch('/allInfluncer',{
            headers:{
                'Authentication-Token':this.token,
            }
        })


        const data = await res.json()
        if(res.ok){
            this.allCampaign = data
        }
    }
}

</script>