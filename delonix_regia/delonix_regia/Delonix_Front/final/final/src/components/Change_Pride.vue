<template>
    <!-- qmanimation_play="|undefined"模仿QQ邮箱弹出动画 -->
    <div class="pride_information" qmanimation_play="|undefined">
        <div style="cursor:move;" class="dialog_head">
            <span>获得荣誉</span>
        </div>

        <!-- 编辑荣誉资料 -->
        <div class="pride_neirong">
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <!-- 时间和奖项的提示 -->
            <div class="tishi">
                <td>
                    <tr>
                        <label style="width: 80px;height: 24px;text-align:center;">时间&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                        <label style="width:250px;height: 24px;text-align:center;">&nbsp;&nbsp;荣誉</label>
                    </tr>
                </td>
            </div>
            <!-- 编辑1 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride1time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride1">
                </div>
            </div>

            <!-- 编辑2 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride2time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride2">
                </div>
            </div>

            <!-- 编辑3 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride3time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride3">
                </div>
            </div>

            <!-- 编辑4 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride4time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride4">
                </div>
            </div>

            <!-- 编辑5 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride5time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride5">
                </div>
            </div>

            <!-- 编辑6 -->
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="normal_change">
                <!-- 时间 -->
                <div class="time">
                    <input class="time_input" id="pride6time">
                </div>
                <!-- 荣誉 -->
                <div class="pride">
                    <input class="pride_input" id="pride6">
                </div>
            </div>

            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
        </div>
        <!-- 保存和取消修改 -->
            <div class="Yes_no_change_btn">
                <button class="btn1">保存</button>
                <button class="btn2" @click="hidden">取消</button>
            </div>
    </div>
</template>

<style>
.pride_information{
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
        height:40px;
    }
    .time{
        float: left;
        width: 80px;
        margin-left: 20px;
        height: 24px;
    }
    .pride{
        float: left;
        margin-left: 10px;
    }
    .time_input{
        width: 80px;
        height: 24px;
        border-radius:3px;
        border: 1px solid #c3c3c3;
        border-top: 1px solid #7c7c7c;
        border-left: 1px solid #9a9a9a;
    }
    .pride_input{
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

<script>
export default {
    name:"PrideInformation",
    data(){
        return{
            pride1time:"",
            pride1:"",
            pride2time:"",
            pride2:"",
            pride3time:"",
            pride3:"",
            pride4time:"",
            pride4:"",
            pride5time:"",
            pride5:"",
            pride6time:"",
            pride6:"",
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
