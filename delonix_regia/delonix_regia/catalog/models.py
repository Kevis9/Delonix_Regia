from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Userprofile(models.Model):
    #作为主键
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',primary_key=True)
    #基本信息
    phonenumber=models.CharField('电话号码', max_length=128)
    name=models.CharField('姓名', max_length=128)
    gender = models.CharField('性别', max_length=128,default="")
    age = models.CharField("年龄", max_length=128,default="")
    city = models.CharField("城市", max_length=128,default="")
    major = models.CharField("专业", max_length=128,default="")
    email = models.CharField("邮件", max_length=128,default="")

    #下面都是模型的元数据设置,方便管理
    class Meta:
        verbose_name = 'User Profile'
    def __str__(self):
        return "{}".format(self.user)
    def get_absolute_url(self):
        # return "/catalog/user/%i/get_profile/" % self.id
        return reverse('get_profile', args=[self.user.id])
        #但是推荐用上面的

