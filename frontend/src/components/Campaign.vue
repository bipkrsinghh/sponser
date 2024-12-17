<template>
    <div v-for="(campaign,index) in allCampaign" :key="campaign.id">
        <div class="bg-green">
            {{ campaign.c_name }}
            <RouterLink :to="{name:'CreateAd',params:{campaignId : campaign.id}}">Add ad</RouterLink>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            allCampaign:[],
            token : localStorage.getItem('auth-token'),
        }
    },

    async mounted(){
        const res = await fetch('/allCampaign',{
            headers:{
                'Authentication-Token':this.token,
            }
        })


        const data = await res.json()
        console.log(res.ok,data)
        if(res.ok){
            this.allCampaign = data
        }
    }
}

</script>