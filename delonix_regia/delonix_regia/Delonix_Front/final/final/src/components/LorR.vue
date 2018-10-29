<template>
  <div id="lorr">
    <router-view/>
    <router-link id="login" to="L">登陆</router-link>
    <router-link id="reg2" to="R">注册</router-link>
  </div>
</template>

<script>
export default {
  name: 'LorR'
}
</script>

<style>
  #lorr{
    background-image: url('../../static/BG6.jpg');
    text-align: center;
    height: 100%;
    width: 100%;
    position: absolute;
  }
  #login{
    color: rgb(84, 122, 226);
    padding: 0px 95px 1px 90px;
    background-color: rgb(205, 222, 248);
    border: 1px solid rgb(36, 98, 200);
    box-shadow: 0 0 2px;
  }
  #reg2{
    color: rgb(84, 122, 226);
    padding: 0px 90px 1px 95px;
    background-color: rgb(205, 222, 248);
    border: 1px solid rgb(36, 98, 200);
    box-shadow: 0 0 2px;
  }
</style>
