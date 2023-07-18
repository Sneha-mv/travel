from django.urls import path
from .import views

urlpatterns=[
     path('', views.staticweb, name='static'),
     path('hi/',views.demo,name='demo'),
     path('hello/',views.hello,name='hello'),
     path('home/',views.home,name='home'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('detail/',views.detail,name='detail'),
     path('thanks/',views.thanks,name='thanks'),
     path('first/',views.first,name='first'),
     path('result/',views.addition,name='addition'),


]
