<template>
<div>
        <div class="ShowSelfDescription"  @click="pop_change_self_func">
                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">自我评价</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <label for="selfdescpt" style="padding-left: 70px;">热爱互联网行业，关注行业动态,学习能力强，对新事物充满好奇,工作态度认真负责，具有团队合作精神。</label>      
            </div>
                  <div><self_description_change v-show="if_show" @hidden="hidden_change_self_func"></self_description_change></div>            
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
    .ShowSelfDescription:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import self_description_change from "@/components/Change_Self_Desc"
import simple_mask from "@/components/Simple_Mask"

export default {
  name: 'ShowSelfDescription',
  data(){
        return{
          selfdescpt:"",
          if_show :false
        }
    },
    components:{
        self_description_change,
        simple_mask,
    },
    mounted(){

    },

    methods:{
        pop_change_self_func:function(){
            this.if_show=true;
        },
        hidden_change_self_func:function(){
            let that = this;
            that.if_show=false;
        }
    },
}
</script>
