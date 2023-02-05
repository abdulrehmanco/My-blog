from django.contrib import admin
from django.urls import path
from home import views
from .views import coldwar, homeveiw


urlpatterns = [

    path('', coldwar.as_view(), name='coldwar'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('home', coldwar.as_view(), name='coldwar'),
    path('coldwar', coldwar.as_view(), name='coldwar'),
    path('postcomment',views.postcomment,name='postcomment'),
    path('<slug:slug>', views.detail, name='detail'),
]

