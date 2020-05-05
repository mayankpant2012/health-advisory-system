from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import LoginForm, UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .models import Report
from .forms import ReportForm
# Create your views here.
'''
def index(request):
    return render(request,'health_adv/index.html')
'''

def index(request):
    context = {
        'login_form': LoginForm(),
        'signup_form': UserCreateForm(),
    }
    return render(request, 'health_adv_app/index.html', context)

def thanks(request):
    return render(request,'accounts/thanks.html')

def about(request):
    return render(request,'health_adv_app/about_us.html')

def contact(request):
    return render(request,'health_adv_app/contact_us.html')

def test(request):
    return render(request, 'health_adv_app/test.html')


@login_required
def user_home(request):
    return render(request, 'health_adv_app/user_home.html')


class CreateReport(LoginRequiredMixin, CreateView):
    login_url = '/'
    #redirect_field_name = 'accounts/test.html'
    success_url = reverse_lazy('health_adv_app:user_home')#redirect to user_home.html
    form_class = ReportForm
    model = Report
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.calculate_bmi()
        form.instance.calculate_diabetes()
        return super().form_valid(form)
