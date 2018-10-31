<template>
<div>
    <div class="ShowJobInformation" @click="pop_change_job_func" >
                <div style="font-size: 1px;height: 6px; line-height: 6px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">就业状况</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="job_basic" style="padding-left: 70px;">                    
                        <label for="job" >工作:项目经理&nbsp;&nbsp;</label>
                        <br>                        
                        <label for="workingplace">工作地点:深圳&nbsp;&nbsp;</label>
                        <br>                                        
                        <label for="livingplace">居住地:深圳&nbsp;&nbsp;</label>                        
                        <br>
                        <label for="annualsalary">年薪:30w&nbsp;&nbsp;</label>                    
                        <br>
     </div>    
      </div>   
            <div><change_job_info v-show="if_show" @hidden="hidden_change_job_func" :if_show_mask="if_show_mask"></change_job_info></div> 
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
    .ShowJobInformation:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import change_job_info from "@/components/Change_Job_Info"
import simple_mask from "@/components/Simple_Mask"

export default {
  name: 'ShowJobInformation',
  data(){
        return{
            job:"",
            livingplace:"",
            annualsalary:"",
            if_show :false,
            if_show_mask:true,
        }
    },    
  components:{
    change_job_info,
    simple_mask,

  },
  methods:{
    pop_change_job_func:function(){
            this.if_show=true;
    },
    hidden_change_job_func:function(){
        let that = this;
        that.if_show=false;
    }
  },
  mounted:function(){
      
  }
}
</script>
