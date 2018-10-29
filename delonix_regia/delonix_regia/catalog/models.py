from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',primary_key=True)
    phonenumber=models.CharField('电话号码', max_length=128)
    name=models.CharField('姓名', max_length=128)


    class Meta:
        verbose_name = 'User Profile'


    def __str__(self):
        return "{}".format(self.user)


    def get_absolute_url(self):
        # return "/catalog/user/%i/get_profile/" % self.id
        return reverse('get_profile', args=[self.user.id])
        #但是推荐用上面的

