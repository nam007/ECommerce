from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import login, authenticate

urlpatterns = [
    	 path('', views.index, name='index'),
    	 url(r'^signup/$', views.signup, name='signup'),
    ]