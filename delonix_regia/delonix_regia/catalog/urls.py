from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.urls import re_path
from django.views.generic.base import TemplateView


urlpatterns=[
    #保证这个应用里面的都是接口，是给前端提供数据的接口
    path('user/login/',views.login_user),
    path('user/<int:pk>/update_top_profile/',views.update_top_profile,name='update_top_profile'),
    path('user/<int:pk>/get_profile/', views.get_profile, name='get_profile'),
    # path('user/<int:pk>/get_profile/',views.get_profile,name='get_profile'),# id是指user的id
]

