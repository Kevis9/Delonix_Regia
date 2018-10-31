<template>
  <div id="loginview">
     <load>
      <h1 id="title">{{title}}
        <h2 id="title2">
          {{title2}}
        </h2>
      </h1>
      <lo>
       <L1 >
        <input id="name" type="text" v-model="name"  placeholder="用户名或邮箱" autocomplete="on">
       </L1>
       <br/>
       <L1 >
       <input id="passkey" type="password" v-model="passkey" placeholder="密码" autocomplete="on">
       </L1>
       <L1 id="change">
         <input type="checkbox" id="checkbox2" v-model="check2">
       </L1>
        <br/>
       <L1 id="remember">
        <input type="checkbox" id="checkbox" v-model="check">
        <label for="checkbox">{{checkbox}}</label>
       </L1>
        <br/>

      <button id="pass" type="submit" @click="login_user_in">
        登录
       </button>
        <br/>
        <router-view/>
        <router-link to="forgetPW">忘记密码</router-link>
      </lo>
     </load>
  </div>
</template>

<script>
export default {
  name: 'login',
  data: function () {
    return {
      title: '凤凰涅槃',
      title2: 'Phoenix Nirvana',
      name: '',
      passkey: '',
      check: true,
      check2: true,
      checkbox: '记住密码',
      msg:'',
    }
  },
  methods:{
     login_user_in:function(){
                const self = this;
                var url="http://127.0.0.1:8000/data/user/login/";               
                this.$http.get(url); //产生COOKIE 必须先get一次不然会报错csrf not set
                var DjangoCookie=getCookie('csrftoken');
                console.log(DjangoCookie);                  
                var senddate={"username":this.name,"password":this.passkey};
                console.log("在之前");                  
                this.$http.post(url,senddate,{headers:{'X-CSRFToken':DjangoCookie}},{emulateJSON: true})
                .then(function(response){ 
                    console.log("拿到了response");                  
                    console.log(response);
                    var res = response.data;
                    if(res.msg=='success')
                        {
                            console.log("yes");
                            self.$router.push({name:"mainpage"});
                        }
                    else
                    {
                        alert(res.msg);
                    }
                    }).catch(function(){
                        alert("服务器有点皮");
                    })
            },
  }
 
}
 function getCookie(name){  //获取cookie函数
    name = name + "=";
    var start = document.cookie.indexOf(name),
        value = null;
    if(start>-1){
        var end = document.cookie.indexOf(";",start);
        if(end == -1){
            end = document.cookie.length;
        }
        value = document.cookie.substring(start+name.length,end);
    }
    return value;
}
function sleep(numberMillis) {   //等待函数
    var now = new Date();
    var exitTime = now.getTime() + numberMillis;
    while (true) {
        now = new Date();
        if (now.getTime() > exitTime)
            return;
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #loginview{
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
  color: rgb(84, 122, 226);
}
#name{
  margin-top: 20px;
  font-size: 18px;
  width: 240px;
  color: #547ae2;
  border: 1px solid #ccc;
  border-radius: 3px;
  -webkit-box-shadow: inset 0 1px 1px  rgba(30,20,200, 0.7);
  box-shadow: inset 0 1px 1px rgba(30, 20, 200, 0.7);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
#passkey{
  font-size: 18px;
  width: 240px;
  margin-top:20px;
  margin-left: 30px;
  border-radius:3px;
  border: 1px solid #ccc;
  -webkit-box-shadow: inset 0 1px 1px rgba(36, 98, 200, 0.7);
  box-shadow: inset 0 1px 1px rgba(36, 98, 200, 0.7);
  -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s
}
#pass{
  color: rgb(84, 122, 226);
  border-color: rgba(75, 192, 247,0.5);
  background-color: rgba(248, 248, 248,0.5);
  width: 240px;
  height: 30px;
  font-size: 15px;
  margin-top:60px;
  border-radius:3px;
  border: 0.5px solid #ccc;
}
#remember{
  font-size: 14px;
  font-family:PingFang SC;
}
</style>
