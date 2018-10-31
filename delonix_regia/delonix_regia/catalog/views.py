from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm,UserprofileForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from .models import Userprofile
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.middleware.csrf import get_token ,rotate_token
import simplejson


def login_user(request):
    if request.method=="POST":
        msg = 'success'
        req=simplejson.loads(request.body)
        username=req['username']
        password=req['password']
        try:
            user_a = User.objects.get(username=username)  # 这个设置是为了更详细的检查出错误来,因为这个地方get函数不会返回none，一旦找不到，便会给一个exception
            user = authenticate(username=username, password=password)  # 而authenticate就能返回一个none
            if user is not None and user.is_active:  # 不要用 password==password 我试过，就算密码正确也是不相等的，因为一个是hash str，一个是str
                login(request,user)
                return JsonResponse({'user_id':user.id,'msg':msg})
                # 旧方法return redirect(reverse("get_profile", args=[user.id]))
            else:
                msg = "请输入正确的密码"
        except Exception as e:
            msg = "用户不存在"
        return JsonResponse({'msg': msg, 'username': username, 'password': password})
    # return render(request,"log_login.html",locals())#locals()应该包括 login_form和msg
    get_token(request)  # 产生一个token
    return JsonResponse({'username': "", 'password': ""})



@login_required(login_url="/delonix_regia/log_in/")
def get_profile(request,pk):
    user=get_object_or_404(User,pk=pk)
    try:
        userprofile = Userprofile.objects.get(user=user)
        response = {"name": userprofile.name, "phonenum": userprofile.phonenumber}
        return JsonResponse(response)
    except Exception as e:
        userprofile=Userprofile(user=user) #如果用户尚未填写过个人信息，那么展示的将会是一个新生成的个人信息
        userprofile.save()
        response = {"name":userprofile.name,"phonenum":userprofile.phonenumber}
        return JsonResponse(response)
   # return render(request, 'get_profile.html', {'userprofile': userprofile})




@login_required(login_url="/delonix_regia/log_in/")
def update_top_profile(request,pk):
    get_token(request)
    user = get_object_or_404(User,pk=pk)
    userprofile = get_object_or_404(Userprofile, user=user)
    if(request.method=="POST"):
        req = simplejson.loads(request.body)
        userprofile.name=req["name"]
        userprofile.phonenumber = req["phonenum"]
        userprofile.save()
        #数据准备
        req["user_id"]=user.id
        req["name"]=userprofile.name
        req["phonenum"] = userprofile.phonenumber
        req["gender"] = userprofile.gender
        req["age"] = userprofile.age
        req["city"] = userprofile.city
        req["major"] = userprofile.major
        req["email"] = userprofile.email
        return JsonResponse(req)
    req={}
    #数据准备
    req["name"] = userprofile.name
    req["phonenum"] = userprofile.phonenumber
    req["gender"]=userprofile.gender
    req["age"] = userprofile.age
    req["city"] = userprofile.city
    req["major"] = userprofile.major
    req["email"] = userprofile.email
    return JsonResponse(req)


# 这个地方我们还是要try 因为如果用户首先进入修改页面的话，而且没有这个用户的信息的话，也要先生成一个

# try:
#    userprofile = Userprofile.objects.get(user=user)
# except Exception as e:
#   userprofile = Userprofile(user=user)  # 如果用户尚未填写过个人信息，那么展示的将会是一个新生成的个人信息
#  userprofile.save()
# if request.method=="POST":
# userprofileform=UserprofileForm(request.POST)
# if userprofileform.is_valid():
#    userprofile.name=userprofileform.cleaned_data['name']
#    userprofile.phonenumber = userprofileform.cleaned_data['phonenumber']
#    userprofile.save()
#    return redirect(reverse("get_profile",args=[user.id]))
# 表单不正确的工作先给前端去做吧

# else:
#   default_data={"name":userprofile.name,"phonenumber":userprofile.phonenumber}
#    return  JsonResponse(default_data)
#    #return render(request,"update.html",{'userprofileform':userprofileform})
# 这个地方为什么一定要返回一个表单? 也就是说request给的其实也就是一串字符串，根据label来给数据?

























