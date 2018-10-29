<template>
    <div class="photo_change" qmanimation_play="|undefined">
        <div style="cursor:move;" class="dialog_head">
            <span>编辑头像</span>
        </div>

        <!-- 整个大框 -->
        <div class="change_photo">
            <!-- 稍大的框 -->
            <div class="main_photo" id="mainphoto">
                暂无头像
            </div>
        </div>

        <div style="margin-top:20px;">
            <button class="upload" id="uploadbtn">从本地上传</button>
        </div>

        <!-- 保存和取消修改 -->
        <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
        <div class="Yes_no_change_btn">
            <button class="btn1" id="save">保存</button>
            <button class="btn2" id="quit">取消</button>
        </div>
    </div>
</template>

<style>
    .photo_change{
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
    .change_photo{
        overflow:hidden;
        zoom:1;
        padding:52px 0 58px 56px; 
    }
    .main_photo{
        position: relative; 
        float:left;
        z-index: 1; 
        width:250px;
        height:200px;
        overflow:hidden;
        border:1px solid #A0A0A0;
        background:#EEEEEE;
        padding-top:117px;
        text-align:center;
        color:#666;
        text-shadow:0 1px 0 #FAFAFA;
    }
    .upload{
        width: 91px; 
        height: 28px; 
        line-height: 28px; 
        font-size: 14px; 
        position: relative;
        margin-left: 60px
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
    name:"PhotoChange",
    data(){
        return{
            mainphoto:"",
            uploadbtn:"",
            save:"",
            quit:""
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>

