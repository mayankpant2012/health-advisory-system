from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfileInfo
from .forms import UserProfileInfoForm, LoginForm, UserCreateForm

from django.shortcuts import render, redirect



def usersignup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            #return reverse_lazy('create_profile')
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:create_profile')
        else:
            return redirect('test')

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('health_adv_app:user_home') #redirect to user_home.html
            else:
                return redirect('thanks')

class CreateUserProfile(LoginRequiredMixin, CreateView):
    login_url = '/'
    #redirect_field_name = 'accounts/test.html'
    success_url = reverse_lazy('health_adv_app:user_home')#redirect to user_home.html
    form_class = UserProfileInfoForm
    model = UserProfileInfo
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    #user attribute of profile is not being defined.


def logged_out(request):
    return render(request,'accounts/logged_out.html')


# make a detail view to display profile details
'''
class Login(auth_views.LoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loginform"]=self.get_form()
        del context["form"]
        return context

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = "health_adv/first_page.html"  #"accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signupform"]=self.get_form()
        del context["form"]
        return context
'''
