<template>
            <div class="ShowSelfDescription" >
                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">自我评价</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <label for="selfdescpt" style="padding-left: 70px;">热爱互联网行业，关注行业动态,学习能力强，对新事物充满好奇,工作态度认真负责，具有团队合作精神。</label>
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
</style>
<script>
export default {
  name: 'ShowSelfDescription',
  data(){
        return{
          selfdescpt:""
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>
