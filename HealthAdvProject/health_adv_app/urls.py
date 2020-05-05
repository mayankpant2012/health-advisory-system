from django.contrib import admin
from django.urls import path,include,re_path
from health_adv_app import views

app_name = 'health_adv_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('user_home/',views.user_home,name='user_home'),
    path('create_report/',views.CreateReport.as_view(),name='create_report'),
]
