"""faceWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from faceDataManagement.views import data, upload_file, index, chouqian
from camera.views import camera, home
from django.views.static import serve

from login.views import login, tologin
from register.views import register

from login.views import facelogin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
    url(r'^data/$', data),
    url(r'^uploadFile/', upload_file),
    url(r'^camera/', facelogin),
    url(r'^$', home),
    url(r'^facePhoto/(?P<path>.*)$', serve, {'document_root': 'facePhoto'}),
    url(r'^chouqian/facePhoto/(?P<path>.*)$', serve, {'document_root': 'facePhoto'}),
    url(r'^chouqian/', chouqian),
    path(r'register/', register),
    path(r'login/', login),
    path(r'logout/', tologin),
]
