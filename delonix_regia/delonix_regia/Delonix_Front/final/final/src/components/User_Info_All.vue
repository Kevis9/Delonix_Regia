<template>
<div id="User_Info_All">
<show_top_info></show_top_info>
<show_school_info></show_school_info>
<show_job_info></show_job_info>
<show_work_info></show_work_info>
<show_pride_info></show_pride_info>
<show_self_desc></show_self_desc>

<!-- <topinformation-vue></topinformation-vue> -->
<!--<router-view class="main" name="showschoolinformation"></router-view>
<router-view class="main" name="showjobinformation"></router-view>
<router-view class="main" name="showworkinformation"></outer-view>
<router-view class="main" name="showprideinformation"></router-view>
<router-view class="main" name="showselfdescription"></router-view> -->
</div>
</template>

<script>
import show_job_info from '@/components/Show_Job_Info'
import show_pride_info from '@/components/Show_Pride_Info'
import show_school_info from '@/components/Show_School_Info'
import show_self_desc from '@/components/Show_Self_Desc'
import show_top_info from '@/components/Show_top_Info'
import show_work_info from '@/components/Show_Work_Info'
export default {

components:{show_pride_info,
            show_job_info,
            show_school_info,
            show_self_desc,
            show_top_info,
            show_work_info,
},

data(){
return{
 }
},

}
</script>