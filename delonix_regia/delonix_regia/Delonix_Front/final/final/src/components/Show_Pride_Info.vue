<template>
<div>
            <div class="ShowPrideInformation" @click="pop_change_pride_func" >
                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">荣誉</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride1time" style="color: #3b3b3b;" width="151">2008</label><!-- 获得时间 --></td>
                        <td><label for="pride1" style=" padding: 0 0 0 4px;">汕头大学三好学生</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>       
            </div>           
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
    .ShowPrideInformation:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import simple_mask from "@/components/Simple_Mask"

import pride_neirong from "@/components/Change_Pride"

export default {
  name: 'ShowPrideInformation',
  data(){
        return{
            //按照名字(name)来取值的
            pride1time:"",
            pride1:"",
            pride2time:"",
            pride2:"",
            if_show :false
        }
    },
    components:{
        pride_neirong,
        simple_mask,
    },
    mounted(){

    },

    methods:{
        pop_change_pride_func:function(){
            this.if_show=true;            
        },
        hidden_change_pride_func:function(){
            let that = this;
            that.if_show=false;
        }
    },
}
</script>