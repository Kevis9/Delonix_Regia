<template>
<div>
    <div class="ShowTopInformation"  @click="pop_change_basicInfo_func">
        <tr>
            <td>
                <div class="top_infor">
                    <div class="basic_information">
                        <label for="name" class="name">五六七</label>
                        <div style="font-size: 1px;height: 3px; line-height: 17px;"></div>
                        <div class="infor_basic" style="padding-left: 70px; color: #374760;">
                            <label for="gender">性别:男&nbsp;&nbsp;</label>
                            <label for="age">年龄:28&nbsp;&nbsp;</label>
                            <label for="city">所在城市:深圳&nbsp;&nbsp;</label>
                            <br>            
                            <label for="learning">学历:硕士&nbsp;&nbsp;</label>
                            <label for="major">专业:计算机科学&nbsp;&nbsp;</label>
                        </div>
                        <div style=" height: 1px; line-height: 1px;"></div> 
                        <div class="infor_basic" style="padding-left: 70px; color: #374760;">
                            <label for="mobile">电话号码:135***0000&nbsp;&nbsp;</label>
                            
                            <br>
                            <label for="email">E-Mail:***@stu.edu.cn&nbsp;&nbsp;</label>
                        </div>    
                    </div>
                </div>
            </td>
            <td>
                <div class="photo" id="mainphoto" width=100 height=140;>
                    
                </div>                
            <td/>
        </tr>       
    </div>
     <div><basic_information_change v-show="if_show" @hidden="hidden_change_basicInfo_func"></basic_information_change></div>
         <div><simple_mask v-show="if_show"></simple_mask></div>

    </div>
</template>

<style>
    .ShowTopInformation{
        padding: 3px 33px 21px 40px; 
        color: #ffff;
        line-height: 1;
    }
    .basic_information{
        font-size: 14px; 
        line-height: 1.5; 
        word-break: break-word; /*在恰当的断字点进行换行*/
        -webkit-font-smoothing: antialiased;/*设置字体的抗锯齿,适合小像素字体*/
        font-family: 'lucida Grande', Verdana, 'Microsoft YaHei';
        padding: 7px;/*上下间距7px*/
        width: 338px;
        height: 90px;
    }
    .name{
        font-size: 34px; 
        font-weight: bold; 
        color: #374760;
        line-height: 1
    }
    .photo{
        padding: 35px 2px 20px 0px; 
        /* color: #ffff; */
        line-height: 0;
        width: 95 ;
        height: 84;
    }
    .iterm_name{
        position: relative; 
        padding: 7px 40px 6px 8px;
        font-size: 16px; 
        font-weight: bold; 
        line-height: 1; 
    }
    .ShowTopInformation:hover{
        background-color:rgba(37, 37, 29, 0.171);
    }
</style>

<script>
import basic_information_change from "@/components/Change_BasicInfo"
import simple_mask from  "@/components/Simple_Mask"
export default {
  name: 'ShowTopInformation',
  data(){
        return{
            name:"",
            gender:"",
            age:"",
            city:"",
            major:"",
            learning:"",
            mobile:"",
            email:"",
            mainphoto:"",
            if_show :false

        }
    },
    components:{
        basic_information_change,
        simple_mask
    },
    mounted(){

    },

    methods:{
        pop_change_basicInfo_func:function(){
            this.if_show=true;
        },
        hidden_change_basicInfo_func:function(){
            let that = this;
            that.if_show=false;
        }
    },
}
</script>