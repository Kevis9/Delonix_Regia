<template>
    <div class="ShowWorkInformation">
            <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
            <div class="iterm_name">职业经历</div>
            <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
            <div class="job_experience_information">
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job1time" style="color: #3b3b3b;" width="151">job1time</label><!-- 在职时间 --></td>
                        <td><label for="company1" style=" padding: 0 0 0 4px;">company1</label><!-- 单位名称 --></td>
                    </tr>    
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job2time" style="color: #3b3b3b;" width="151">job2time</label><!-- 在职时间 --></td>
                        <td><label for="company2" style=" padding: 0 0 0 4px;">company2</label><!-- 单位名称 --></td>
                    </tr>    
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job3time" style="color: #3b3b3b;" width="151">job3time</label><!-- 在职时间 --></td>
                        <td><label for="company3" style=" padding: 0 0 0 4px;">company3</label><!-- 单位名称 --></td>
                    </tr>    
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job4time" style="color: #3b3b3b;" width="151">job4time</label><!-- 在职时间 --></td>
                        <td><label for="company4" style=" padding: 0 0 0 4px;">company4</label><!-- 单位名称 --></td>
                    </tr>    
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job5time" style="color: #3b3b3b;" width="151">job5time</label><!-- 在职时间 --></td>
                        <td><label for="company5" style=" padding: 0 0 0 4px;">company5</label><!-- 单位名称 --></td>
                    </tr>    
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="job6time" style="color: #3b3b3b;" width="151">job6time</label><!-- 在职时间 --></td>
                        <td><label for="company6" style=" padding: 0 0 0 4px;">company6</label><!-- 单位名称 --></td>
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
  name: 'ShowWorkInformation',
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
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>