<template>
            <div class="ShowPrideInformation">
                <div style="font-size: 1px;height: 17px; line-height: 17px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">荣誉</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride1time" style="color: #3b3b3b;" width="151">pride1time</label><!-- 获得时间 --></td>
                        <td><label for="pride1" style=" padding: 0 0 0 4px;">pride1</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride2time" style="color: #3b3b3b;" width="151">pride2time</label><!-- 获得时间 --></td>
                        <td><label for="pride2" style=" padding: 0 0 0 4px;">pride2</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride3time" style="color: #3b3b3b;" width="151">pride3time</label><!-- 获得时间 --></td>
                        <td><label for="pride3" style=" padding: 0 0 0 4px;">pride3</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride4time" style="color: #3b3b3b;" width="151">pride4time</label><!-- 获得时间 --></td>
                        <td><label for="pride4" style=" padding: 0 0 0 4px;">pride4</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride5time" style="color: #3b3b3b;" width="151">pride5time</label><!-- 获得时间 --></td>
                        <td><label for="pride5" style=" padding: 0 0 0 4px;">pride5</label><!-- 荣誉名称 --></td>
                    </tr>   
                </div>
                <div class="per_one" style="padding-left: 70px;">
                    <tr>
                        <td><label for="pride6time" style="color: #3b3b3b;" width="151">pride6time</label><!-- 获得时间 --></td>
                        <td><label for="pride6" style=" padding: 0 0 0 4px;">pride6</label><!-- 荣誉名称 --></td>
                    </tr>   
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
  name: 'ShowPrideInformation',
  data(){
        return{
            //按照名字(name)来取值的
            pride1time:"",
            pride1:"",
            pride2time:"",
            pride2:""
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>