<template>
	<div id="div1">
	<!-- <img src="../assets/background.jpg"/></div>	 -->
           <div id = "one">
			<div id="title">
				<img src="../assets/stu.png" width="50px" height="50px" id="imgSet">
				<h1 id="titleHead">凤凰花开 </h1>
				<h2 id="englishTitle">Phoenix Nirvana</h2>
				<button class="button" style="vertical-align:middle"><span><router-link to="LorR">退出登录</router-link></span></button>
			</div>
		  </div>        
          <div id="leftPart">     <!-- wholeleftPart -->
			<div  class="leftTop">    <!-- lefttop，个人信息 -->
			<div id="imgAndName">
				
				<!-- <span style="width: 50px"></span>
 -->				<img src="../assets/clock.jpg" id="headImg" v-on:click = "show = ! show">
			    
			   <!--  <div id="fashionName">
				<lable style="text-align:left">昵称：</lable>
				<textarea id="textArea1"  rows="2" cols="10" disabled>STU</textarea>
			    </div> -->
				<transition name = "fade">
			    	<div  v-show="show" id="fashionName">
			    		<label>昵称</label>  <br>
			    		<br>
			    		<textarea  style="background: none; height:40px;width: 80px;border: none;text-align: center;" >STU</textarea>
			    		<lable>个性签名：</lable>  <br>    
						<textarea id="textArea2" rows="6" cols="20" disabled>汕大牛逼</textarea>
					</div>
				</transition>	
								
			    	</div>
			
            
			</div>

				<div class="container">
								<div class="link">
									<!-- <div class="text"><a href="#">个人信息</a></div> -->
						 			<div class="text"><router-link to="user_info_all">个人信息</router-link></div>
								</div>

								<div class="link">
									<div class="text"><router-link to="test1">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test2">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test">系统更新中</router-link></div>
								</div>
								<div class="link">
									<div class="text"><router-link to="test">系统更新中</router-link></div>
								</div>
								
							</div>
	</div>
	<div id="rightPart" >
           
		   <router-view/>
		</div>
</div>
		
		 

<!-- $(document).ready(function(){
	$("#headImg").click(
     function() {
     	 $("#fashionName").slideToggle("slow")
     }
		)
}) -->

</template>

<script>

export default {
  name: 'MainPage',
  data : function() {
	  return {
		  show : false
	  }
  },
  methods : {
	  imgClicked : function() {
		  $("#fashionName").slideToggle("slow")
	  }
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
    transition: opacity 2s
}
.fade-enter, .fade-leave-to /* .fade-leave-active, 2.1.8 版本以下 */ {
    opacity: 0
}
#imgSet,#titleHead,#englishTitle
	{
		float:left;
	}
	#one
	{
		width:100%;
		height:13%;
	}
	.button
	{

		float:right;
	}
	
	#leftPart
	{
		width:18%;
		height:87%;
		float:left;
		
	}
	.leftTop
	{
		width:75%;
		background:rgba(0, 0, 0, 0.75);
		margin:0px auto;
		padding:20px 20px 20px 20px; 
		border:1px solid #111;
		border-radius:10px;
		box-shadow:0px 4px 5px rgba(0, 0, 0, 0.75);
	}
	/*#leftMiddle
	{
		height:2%;
/*		background: green;
*/	
#imgAndName
	{
		width:100%;
		height:50%;
		
		text-align: center;
	}
	#imageSetting
	{
		/*float:left;*/
		width:100%;
		height:50%;
	}
	#fashionName
	{
		height:70px;
		width:80px;
	   /*width:100px;*/
	   /*border:1px solid;*/
	    margin:10px;
		color:black;
		background: none;
	}
	
	#rightPart
	{
		border:1px solid green;
		border-radius: 10px;
		background-color:rgba(255,255,255,0.9);
		margin-left: 10px;
		margin-right: 0;
		width:80.5%;
		height:87%;
		float: left;
		overflow:scroll;
		
	}
.button {
  display: inline-block;
  border-radius: 10px;
  background:rgba(0, 0, 0, 0.75);
  border: none;
  color: rgb(255, 255, 255);
  text-align: center;
  font-size: 15px;
  width: 100px;
  height: 50px;
  float:right;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '»';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

div#div1{
	background-image: url('../../static/background.jpg');
	background-size: cover; 
	background-attachment: fixed;
	position: absolute;
	width: 100%;
	height: 100%;

	/* overflow: hidden; */
	
}
#title
{
	height:60px;
}
#titleHead{
	color: transparent;
    background-color: black;
    text-shadow: rgba(255,255,255,0.5) 0 5px 6px, rgba(255,255,255,0.2) 1px 3px 3px;
    -webkit-background-clip: text;
	letter-spacing: 10px;
	float: left;
	text-align: center;
	font-size: 30px;
}
#englishTitle{
	color: transparent;
    background-color: black;
    text-shadow: rgba(255,255,255,0.5) 0 5px 6px, rgba(255,255,255,0.2) 1px 3px 3px;
    -webkit-background-clip: text;
	word-spacing: 10px;
	float: left;
	text-align: center;
	position: relative;
	margin-top:35px;
	font-size: 15px;
}
#imgSet{
	width:100px;
	height: 80px;
	float:left;
	border-radius: 8px;
}
#headImg{
	height:100px;
	width:100px;
	border:1px solid;
	border-radius: 50%;
	padding:0px,50px;
	/* float:left; */
}
/*#textArea1{
	width:90px;
	height:70px;
	font-style:italic;
	font-weight: bold;
	font-size: 15px;
	background: none;
	border:none;
	text-align:center;
}*/
#textArea2{
	width:200px;
	height:60px;
	font-style:italic;
	font-weight: bold;
	font-size: 15px;
    background: none;
    border:none;
	text-align:center;
	padding-top: 10px;
	padding-bottom: 0px;
}
.container{
   width:75%;
   background:rgba(0, 0, 0, 0.75);
   margin:10px auto;
   padding:20px 20px 20px 20px;
   border:1px solid #111;
   border-radius:4px;
   box-shadow:0px 4px 5px rgba(0, 0, 0, 0.75);
}
.link{
   font-size:16px;
   font-weight:300;
   text-align:center;
   position:relative;
   height:40px;
   line-height:40px;
   margin-top:8px;
   overflow:hidden;
   width:90%;
   margin-left:5%;
   cursor:pointer;
}
.link a{
	text-decoration: none;
}
.link:after{
   content: '';
   position:absolute;
   width:80%;
   border-bottom:1px solid rgba(255, 255, 255, 0.5);
   bottom:50%;
   left:-100%;
   transition-delay: all 0.5s;
   transition: all 0.5s;
}
.link:hover:after,
.link.hover:after{
   left:100%;
}
.link .text{
   text-shadow:0px -40px 0px rgba(255, 255, 255, 1);
   transition:all 0.75s;
   transform:translateY(100%) translateZ(0);
   transition-delay:all 0.25s;
}
.link:hover .text,
.link.hover .text{
   text-shadow:0px -40px 0px rgba(255, 255, 255, 0);
   transform:translateY(0%) translateZ(0) scale(1.1);
   font-weight:600;
}
</style>