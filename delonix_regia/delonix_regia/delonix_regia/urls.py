"""delonix_regia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.urls import re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',include('catalog.urls')),
    path('',RedirectView.as_view(url="/catalog/")),
    path('delonix_regia/log_in/',TemplateView.as_view(template_name="index.html")),#//登陆界面
    path('delonix_regia/<int:pk>/',TemplateView.as_view(template_name="get_profile_for_vue.html")),#个人信息界面
    path('delonix_regia/<int:pk>/update_profile/',TemplateView.as_view(template_name="update_profile_for_vue.html")),#更新个人信息的界面
]

