<template>
    <!-- qmanimation_play="|undefined"模仿QQ邮箱弹出动画 -->
    <div class="job_experience" qmanimation_play="|undefined">
        <div style="cursor:move;" class="dialog_head">
            <span>职业经历</span>
        </div>

        <!-- 编辑职业资料 -->
        <div class="education_neirong">
            <div class="tishi">
                <td>
                    <tr>
                        <label style="width: 80px;height: 24px;text-align:center;">时间&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                        <label style="width:250px;height: 24px;text-align:center;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;荣誉</label>
                    </tr>
                </td>
            </div>
            <!-- 编辑1 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job1time">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company1">
                </div>
            </div>

            <!-- 编辑2 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job2time">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company2">
                </div>
            </div>


            <!-- 编辑3 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job3time">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company3">
                </div>
            </div>


            <!-- 编辑4 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job4time">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company4">
                </div>
            </div>

            <!-- 编辑5 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job5time">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company5">
                </div>
            </div>


            <!-- 编辑6 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time2">
                    <input class="time_input" id="job6time2">
                </div>
                <!-- 单位 -->
                <div class="company">
                    <input class="company_input" id="company6">
                </div>
            </div>
        </div>

        <!-- 保存和取消修改 -->
        <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
        <div class="Yes_no_change_btn">
            <button class="btn1" id="save">保存</button>
            <button class="btn2" id="quit" @click="hidden">取消</button>
        </div>
    </div>
</template>

<script>
export default {
    name:"JobExperience",
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
            save:"",
            qiut:""

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

<style>
.job_experience{
        font-size: 14px;
        z-index: 1120; 
        position: absolute; 
        width: 506px; 
        opacity: 1; 
        left: 494px; 
        top: 55px; 
        margin-top: 0px;
        overflow: scroll;
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
    .tishi{
        padding-left: 40px;
        margin-left: 20px;
        width: auto;
    }
    .normal_change{
        width: auto;
        position: relative;
        padding-left: 20px;
        margin-left: 20px;
        height:70px;
    }
    .normal_label{
        height: 28px;
        zoom: 1;
        padding-left: 10px
    }
    .time1{
        float: left;
        width: 40px;
        margin-left: 20px;
        height: 24px;
    }
    .time_label{   
        float: left;
        margin: 0 4px;
        width: 10px;
        height:24px;
        padding: 0 4px;
        align-items:center;
    }
    .label_shili{
        text-align: center;
        width: 10px;
        height:24px;
        float: none;
    }
    .time2{
        margin-left: 2px;
        float: left;
        width: 40px;
        height: 24px;
    }
    .company{
        float: left;
        margin-left: 10px;
    }
    .time_input{
        width: 40px;
        height: 24px;
        border-radius:3px;
        border: 1px solid #c3c3c3;
        border-top: 1px solid #7c7c7c;
        border-left: 1px solid #9a9a9a;
    }
    .company_input{
        width:250px;
        height: 24px;
        border-radius:3px;
        border: 1px solid #c3c3c3;
        border-top: 1px solid #7c7c7c;
        border-left: 1px solid #9a9a9a;
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
