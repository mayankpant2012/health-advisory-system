from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import LoginForm, UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView
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
    report_set = request.user.report_set.all()
    latest_report = 0
    if report_set:
        latest_report = report_set[0]
    return render(request,
                  'health_adv_app/user_home.html',
                  context={'report_set': report_set,
                            'latest_report': latest_report},)


class CreateReport(LoginRequiredMixin, CreateView):
    login_url = '/'
    #redirect_field_name = 'accounts/test.html'
    success_url = reverse_lazy('health_adv_app:user_home')#redirect to user_home.html
    form_class = ReportForm
    model = Report
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.calculate_age()
        form.instance.calculate_bmi()
        form.instance.calculate_fbs()
        form.instance.calculate_diabetes()
        form.instance.calculate_stroke()
        form.instance.calculate_heart_disease()
        return super().form_valid(form)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'health_adv_app/report_detail.html'


class DeleteReportView(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy("health_adv_app:user_home")
