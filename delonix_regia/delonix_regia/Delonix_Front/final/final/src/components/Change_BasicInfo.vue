<template>
    <!-- qmanimation_play="|undefined"模仿QQ邮箱弹出动画 -->
    <div class="basic_information_change" qmanimation_play="|undefined">
        <div style="cursor:move;" class="dialog_head">
            <span>基本资料</span>
        </div>

        <div style="visibility: visible;">
            <!-- 修改资料 -->
            <div class="change_neirong_dialog">
                <!-- 修改内容 -->
                        <!-- 编辑基本信息 -->
                        <div class="change_basic_information">
                            <!-- 编辑姓名、性别、生日（年龄） -->
                            <div class="change_name_gender_birthday">
                                <!-- 编辑姓名 -->
                                <div class="normal_change">
                                    <div>
                                        <label class="normal_label">姓名</label><!-- 很多label标签都是一样的，设置成一个class -->
                                    </div>
                                    <div>
                                        <input class="normal_input" type="text" name="name" id="name" value="" autocomplete="off">
                                    </div>
                                </div>

                                <!-- 编辑性别 -->
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                                <div class="normal_change">
                                    <div>
                                        <label class="normal_label">性别</label>
                                    </div>
                                    <div>
                                        <input class="normal_input" type="text" value="" name="gender" id="gender" autocomplete="off">
                                    </div>                                                                                                                         
                                </div>

                                <!-- 编辑年龄 -->
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                                <div class="normal_change">
                                    <div>
                                        <label class="normal_label">年龄</label>
                                    </div>
                                    <div>
                                        <input class="normal_input" type="text" name="age" id="age" value="" autocomplete="off">
                                    </div>
                                </div>   
                            </div>

                            <!-- 编辑地区 -->
                            <div class="change_city_major_learning">
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                                <div class="normal_change">
                                    <div>
                                        <label class="normal_label">所在城市</label>
                                    </div>
                                    <div>
                                        <input class="normal_input" type="text" name="city" id="city" value="" autocomplete="off">
                                    </div>
                                </div>

                                <!-- 编辑专业 -->
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                                <div class="normal_change">
                                    <div>
                                        <label class="normal_label">专业</label>
                                    </div>
                                <div>
                                    <input class="normal_input" type="text" name="major" id="major" value="" autocomplete="off">
                                </div>
                                
                                <!-- 编辑学历 -->
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                                <div class="normal_change" style="margin-left:2px;">
                                    <div>
                                        <label class="normal_label">最高学历</label>
                                    </div>
                                    <div>
                                        <input class="normal_input" type="text" name="learning" id="learning" value="" autocomplete="off">
                                    </div>
                                </div>
                                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                            </div>
                        </div>

                        <!-- 编辑电话和邮箱 -->
                        <div class="change_phone_mail">
                            <!-- 编辑电话 -->
                            <div class="normal_change">
                                <div>
                                    <label class="normal_label">手机</label>
                                </div>
                                <div>
                                    <input class="normal_input" type="text" name="mobile" id="mobile" value="" autocomplete="off">
                                </div>
                            </div>

                            <!-- 编辑邮箱 -->
                            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                            <div class="normal_change">
                                <div>
                                    <label class="normal_label">邮箱</label>
                                </div>                      
                                <div>
                                    <input class="normal_input" type="text"  name="email" id="email" value="" autocomplete="off">
                                </div>
                            </div>    
                            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->                   
                        </div>                       
                </div>
            </div>

            <!-- 保存和取消修改 -->
            <div class="Yes_no_change_btn">
                <button class="btn1" id="save">保存</button>
                <button class="btn2" id="quit" @click="hidden">取消</button>
            </div>
        </div>
    </div>
</template>

<style>
    .basic_information_change{
        font-size: 14px;
        z-index: 1120; 
        position: absolute;
        width: 506px; 
        opacity: 1; 
        left: 494px; 
        top: 55px; 
        margin-top: 0px;
        overflow: hidden;
        border: 1px solid #aaa;
        box-shadow: 0 0 8px rgba(0,0,0,0.2);
        border-radius: 5px;
        min-width: 500px;
        background-color: #ffffff;
        -webkit-font-smoothing: antialiased;
        font-family: "lucida Grande",Verdana,"Microsoft YaHei";
    }
    .dialog_head {
        background-color: #eaeaea;
        padding: 5px 15px;
        line-height: 25px;
        font-weight: bold;
        border-radius: 5px 5px 0 0;
        border-bottom: 1px solid #ccc;
    }
    .dialog_content{
        width: 100%; 
        max-height: 520px; 
        overflow: auto; 
        position: relative;
    }
    .normal_change{
        width: auto;
        position: relative;
        margin-left: 60px;
    }
    .mormal_label{
        height: 28px;
        line-height: 28px;
        overflow: hidden;
        zoom: 1;
        cursor: default;
        text-align: right;
    }
    .normal_input{
        display: block;
        width: 300px;
        height: 14px;
        margin: 0;
        padding: 7px 8px;
        background-color: #fff;
        border: 1px solid #c3c3c3;
        border-top: 1px solid #7c7c7c;
        border-left: 1px solid #9a9a9a;
        font-size: 14px;
        line-height: 16px;
        color: #000;
        box-shadow: inset 0 1px 0 #d4d4d4;
        outline: none;
        border-radius:7px;
    }
    .Yes_no_change_btn{
        padding-right: 0;
        padding-left: 0;
        background-color: #eaeaea;
        padding: 6px 12px;
        text-align: right;
        line-height: 25px;
        border-top: 1px solid #ccc;
        display: block;
    }
    .btn1{
        margin: 0 0 1px 3px;
        text-decoration: none;
        margin-right: 10px!important;
        padding: 0 200 0 20px;
        height: 24px;
        width: 80px;
        border: 1px solid #1d567d;
        border-radius: 8px;
        color: #fff;
        background: #2e89c5;
        background: -moz-linear-gradient(top,#2a96d8 0%,#257db9 90%,#2e89c5 100%);
        background: -webkit-linear-gradient(top,#2a96d8 0%,#257db9 90%,#2e89c5 100%);
    }
    .btn2{
        margin: 0 0 1px 3px;
        margin-right: 10px!important;
        padding: 0 200 0 20px;
        height: 24px;
        width: 80px;
        min-width: 24px;
        text-decoration: none;
        cursor: default;
        border-radius: 8px;
        color: #000000;
        background: #F3F3F3;
        background: -moz-linear-gradient(top,#ffffff 0%,#ebebeb 90%,#F3F3F3 100%);
        background: -webkit-linear-gradient(top,#ffffff 0%,#ebebeb 90%,#F3F3F3 100%);
    }
</style>
<script>
export default {
    name:"BasicInformationChange",
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
            save:"",
            quit:""
        }
    },

    mounted(){

    },

    methods:{
        hidden:function(){        
        this.$emit('hidden');
      }
    },
}
</script>

