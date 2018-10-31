<template>
<div>
            <div class="ShowSchoolInformation" @click="pop_change_edu_func" >
                <div style="font-size: 1px;height: 6px; line-height: 6px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">教育经历</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="edu_neirong" style="padding: 0 0 7px 40px; ">
                    <div class="per_one" style="padding-left: 40px;">
                        <!-- td,tr,是为了将两个div并列在一行 -->
                      
                            <label for="pritime" style="color: #3b3b3b;" width="151"> 在校时间:2005-2009</label><!-- 在校时间 -->
                            <br>
                            <label for="pri" style=" padding: 0 0 0 4px;">学校名称:汕头大学</label><!-- 学校名称 -->  
                    
                    </div>                    
                    
                </div>
     
            </div>
    <div><education_neirong v-show="if_show" @hidden="hidden_change_edu_func"></education_neirong></div>
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
    .ShowSchoolInformation:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import education_neirong from "@/components/Change_Edu"
import simple_mask from "@/components/Simple_Mask"

export default {
  name: 'ShowSchoolInformation',
  data(){
        return{
            pritime:"",
            pri:"",
            midtime:"",
            mid:"",
            hightime:"",
            high:"",
            unitime:"",
            uni:"",
            mastime:"",
            mas:"",
            phdtime:"",
            phd:"",
            if_show :false
        }
    },
    components:{
        education_neirong,
        simple_mask,
    },
    mounted(){

    },

    methods:{
        pop_change_edu_func:function(){
            this.if_show=true;
        },
        hidden_change_edu_func:function(){
            let that = this;
            that.if_show=false;
        }
    },
}
</script>
