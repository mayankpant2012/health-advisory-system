from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    #path("login/", views.Login.as_view(template_name="health_adv/first_page.html"),name='login'),
    path("login/", views.userlogin,name='login'),

    path("logout/",auth_views.LogoutView.as_view(next_page=reverse_lazy('health_adv_app:index')),name="logout"),

    #path("signup/", views.SignUp.as_view(), name="signup"),
    path("signup/", views.usersignup, name="signup"),
    path("create_profile/", views.CreateUserProfile.as_view(), name="create_profile"),
    path('logged_out/',views.logged_out,name='logged_out'),
    #path for userhome
]
