from django.contrib import admin
from django.urls import path,include,re_path
from health_adv_app import views

app_name = 'health_adv_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
