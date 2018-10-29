<template>
    <div class="ShowJobInformation">
                <div style="font-size: 1px;height: 6px; line-height: 6px;"></div><!-- 间隔的空白 -->
                <div class="iterm_name">就业状况</div>
                <div style=" height: 1px; background-color: #e8e8e8; line-height: 1px; font-size: 1px;"></div><!-- 间隔的线 -->
                <div class="job_basic" style="padding-left: 70px;">
                    <td>
                        <tr><label for="job" >job&nbsp;&nbsp;</label></tr>
                        <tr><label for="workingplace">workingplace&nbsp;&nbsp;</label></tr>
                    </td>
                    <td>
                        <label for="livingplace">livingplace&nbsp;&nbsp;</label>
                        <label for="annualsalary">annualsalary&nbsp;&nbsp;</label>
                    </td>
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
  name: 'ShowJobInformation',
  data(){
        return{
            job:"",
            livingplace:"",
            annualsalary:""
        }
    },

    mounted(){

    },

    method(){

    },
}
</script>
