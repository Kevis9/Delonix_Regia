<template>
            <div class="ShowSchoolInformation">
                <div style="font-size: 1px;height: 6px; line-height: 6px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">教育经历</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="edu_neirong" style="padding: 0 0 7px 40px; ">
                    <div class="per_one" style="padding-left: 40px;">
                        <!-- td,tr,是为了将两个div并列在一行 -->
                       <tr>
                            <td><label for="pritime" style="color: #3b3b3b;" width="151">pritime</label><!-- 在校时间 --></td>
                            <td><label for="pri" style=" padding: 0 0 0 4px;">pri</label><!-- 学校名称 --></td>    
                        </tr>
                    </div>
                    <div class="per_one" style="padding-left: 40px;">
                        <tr>
                            <td><label for="midtime" style="color: #3b3b3b;" width="151">midtime</label><!-- 在校时间 --></td>
                            <td><label for="mid" style=" padding: 0 0 0 4px;">mid</label><!-- 学校名称 --></td>    
                        </tr>
                    </div>
                    <div class="per_one" style="padding-left: 40px;">
                        <tr>
                            <td><label for="hightime" style="color: #3b3b3b;" width="151">hightime</label><!-- 在校时间 --></td>
                            <td><label for="high" style=" padding: 0 0 0 4px;">high</label><!-- 学校名称 --></td>    
                        </tr>
                    </div>
                    <div class="per_one" style="padding-left: 40px;">
                        <tr>
                            <td><label for="unitime" style="color: #3b3b3b;" width="151">unitime</label><!-- 在校时间 --></td>
                            <td><label for="uni" style=" padding: 0 0 0 4px;">uni</label><!-- 学校名称 --></td>    
                        </tr>
                    </div>
                    <div class="per_one" style="padding-left: 40px;">
                        <tr>
                            <td><label for="mastime" style="color: #3b3b3b;" width="151">mastime</label><!-- 在校时间 --></td>
                            <td><label for="mas" style=" padding: 0 0 0 4px;">mas</label><!-- 学校名称 --></td>    
                        </tr>
                    </div>
                    <div class="per_one" style="padding-left: 40px;">
                        <tr>
                            <td><label for="phdtime" style="color: #3b3b3b;" width="151">phdtime</label><!-- 在校时间 --></td>
                            <td><label for="phd" style=" padding: 0 0 0 4px;">phd</label><!-- 学校名称 --></td>    
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
</style>

<script>
export default {
  name: 'ShowSchoolInformation',
  data(){
        return{
            pritime:"",
            pri:"",
            midtime:"",
            mid:"",
            hightime:"",
            high:"",
            unitime:"",
            uni:"",
            mastime:"",
            mas:"",
            phdtime:"",
            phd:""
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>
