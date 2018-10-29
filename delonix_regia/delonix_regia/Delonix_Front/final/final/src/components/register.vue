<template>
  <div id="reg">
     <load>
      <h1 id="title">{{title}}
        <h2 id="title2">
          {{title2}}
        </h2>
      </h1>
      <lo>
       <L1 >
        <input id="number" type="text" v-model="number"  placeholder="邮箱" autocomplete="on">
        </L1>
       <br/>
       <L1 >
       <input id="checknumber" type="text" v-model="checknumber" placeholder="输入6位邮箱验证码" autocomplete="on">
       </L1>
       <br/>
       <button id="register" type="button">
        注册
       </button>
      </lo>
     </load>
  </div>
</template>

<script>
export default {
  name: 'register',
  data: function () {
    return {
      title: '凤凰涅槃',
      title2: 'Phoenix Nirvana',
      number: '',
      checknumber: ''
    }
  }
}
</script>

<style scoped>
  #reg{
    margin-top: 200px;
  }
#title{
  color: rgb(84, 122, 226);
  text-align: center;
  margin: 0px auto;
  width: 300px;
  font-size: 50px;
}
#title2{
  font-size: 20px;
}
lo{
   font-family:'Courier New', Courier, monospace;
   position: relative;
   top:10px;
}
load{
  margin:0 auto;
  padding: 0.5cm 0.5cm 0.5cm 0.5cm;
  display: block;
  width: 400px;
  height: 350px;
  border: 2px solid rgb(36, 98, 200);
  background-color: white;
  box-shadow: 0 0 5px;
  background: rgb(219, 226, 250);
  color: rgb(30, 199, 241);
  }
#number{
  margin-top: 20px;
  font-size: 18px;
  width: 240px;
  color: #00ffff;
  border: 1px solid #ccc;
  border-radius: 3px;
  -webkit-box-shadow: inset 0 1px 1px  rgba(30,20,200,0.7);
  box-shadow: inset 0 1px 1px rgba(30, 20, 200, 0.7);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
#checknumber{
  font-size: 18px;
  width: 240px;
  margin-top:20px;
  border-radius:3px;
  border: 1px solid #ccc;
  -webkit-box-shadow: inset 0 1px 1px rgba(36, 98, 200, 0.7);
  box-shadow: inset 0 1px 1px rgba(36, 98, 200, 0.7);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
#register{
  color: rgb(84, 122, 226);
  border-color: rgba(75, 192, 247,0.5);
  background-color: rgba(248, 248, 248,0.5);
  width: 240px;
  height: 30px;
  font-size: 15px;
  margin-top:81px;
  margin-right: 8px;
  border-radius:3px;
  border: 0.5px solid #ccc;
  }
</style>
