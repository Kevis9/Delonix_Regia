<template>
    <div class="ShowTopInformation">
        <tr>
            <td>
                <div class="top_infor">
                    <div class="basic_information">
                        <label for="name" class="name">name</label>
                        <div style="font-size: 1px;height: 17px; line-height: 17px;"></div>
                        <div class="infor_basic" style="padding-left: 70px; color: #374760;">
                            <label for="gender">gender&nbsp;&nbsp;</label>
                            <label for="age">age&nbsp;&nbsp;</label>
                            <label for="city">city&nbsp;&nbsp;</label>
                            <label for="learning">learning&nbsp;&nbsp;</label>
                            <label for="major">major&nbsp;&nbsp;</label>
                        </div>
                        <div style=" height: 1px; line-height: 1px;"></div> 
                        <div class="infor_basic" style="padding-left: 70px; color: #374760;">
                            <label for="mobile">mobile&nbsp;&nbsp;</label>
                            <label for="email">email&nbsp;&nbsp;</label>
                        </div>    
                    </div>
                </div>
            </td>
            <td>
                <div class="photo" id="mainphoto" width=100 height=140;>
                    <img class="self_photo" src="C:\Users\asus\Desktop\information\src/assets/logo.png">
                </div>
            <td/>
        </tr>
    </div>
</template>

<style>
    .ShowTopInformation{
        padding: 66px 33px 21px 40px; 
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
</style>

<script>
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
            mainphoto:""

        }
    },

    mounted(){

    },

    method(){

    },
}
</script>