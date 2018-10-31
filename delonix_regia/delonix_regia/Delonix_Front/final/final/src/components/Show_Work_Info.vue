<template>
<div>
    <div class="ShowWorkInformation"  @click="pop_change_jobExe_func">
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="iterm_name">职业经历</div>
            <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
            <div class="job_experience_information">
                <div class="per_one" style="padding-left: 70px;">
                    
                        <label for="job1time" style="color: #3b3b3b;" width="151">在职时间:2010-至今</label><!-- 在职时间 -->
                        <br>
                        <label for="company1" style=" padding: 0 0 0 4px;">单位:腾讯</label><!-- 单位名称 -->
                                     
            </div>   
            </div>      
   
    </div>
          <div><change_job_exe v-show="if_show" @hidden="hidden_change_jobExe_func"></change_job_exe></div>
          <div><simple_mask v-show="if_show"></simple_mask></div>

</div>
</template>

<style>
    .iterm_name{
        position: relative; 
        padding: 7px 40px 6px 8px;
        font-size: 16px; 
        font-weight: bold; 
        line-height: 1; 
    }
    .ShowWorkInformation:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import change_job_exe from "@/components/Change_Job_Exe"
import simple_mask from  "@/components/Simple_Mask"

export default {
  name: 'ShowWorkInformation',
  data(){
        return{
            job1time:"",
            job2time:"",
            job3time:"",
            job4time:"",
            job5time:"",
            job6time:"",
            company1:"",
            company2:"",
            company3:"",
            company4:"",
            company5:"",
            company6:"",
            if_show :false
        }
    },
    components:{
        change_job_exe,
        simple_mask,
    },
    mounted(){

    },

    methods:{
        pop_change_jobExe_func:function(){
            this.if_show=true;
        },
        hidden_change_jobExe_func:function(){
            let that = this;
            that.if_show=false;
        }
    },
}
</script>