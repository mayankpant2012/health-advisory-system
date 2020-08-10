from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import LoginForm, UserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Report
from .forms import ReportForm

#for visualization
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
import io
from . graph_plot import make_plot
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
    y_diab = 0
    #make plots from report_set. and save them to latest_report
    # if report_set exists and glucose_plot is empty(which will only happen when report was just generated)
    if report_set and not report_set[0].weight_plot:
        y_glucose = list(Report.objects.values_list('glucose', flat=True).filter(user=request.user).order_by('generation_date'))
        y_weight = list(Report.objects.values_list('weight', flat=True).filter(user=request.user).order_by('generation_date'))
        y_systolic_bp = list(Report.objects.values_list('systolic_bp', flat=True).filter(user=request.user).order_by('generation_date'))
        y_diastolic_bp = list(Report.objects.values_list('diastolic_bp', flat=True).filter(user=request.user).order_by('generation_date'))
        y_cholestrol = list(Report.objects.values_list('cholestrol', flat=True).filter(user=request.user).order_by('generation_date'))

        x_dates = list(Report.objects.values_list('generation_date', flat=True).filter(user=request.user).order_by('generation_date'))

        make_plot_glucose = make_plot('Blood Sugar', x_dates, y_glucose, str(report_set[0].id))
        make_plot_weight = make_plot('Weight', x_dates, y_weight, str(report_set[0].id))
        make_plot_bp = make_plot('Blood Pressure', x_dates, y_systolic_bp, str(report_set[0].id), y_diastolic_bp)
        make_plot_cholestrol = make_plot('Cholestrol', x_dates, y_cholestrol, str(report_set[0].id))

        report_set[0].glucose_plot.save(make_plot_glucose[0],make_plot_glucose[1])
        report_set[0].weight_plot.save(make_plot_weight[0],make_plot_weight[1])
        report_set[0].bp_plot.save(make_plot_bp[0],make_plot_bp[1])
        report_set[0].cholestrol_plot.save(make_plot_cholestrol[0],make_plot_cholestrol[1])

    latest_report = 0
    if report_set:
        latest_report = report_set[0]
    ideal_weight_low = 19 * ((latest_report.user.info.height/100) ** 2)
    ideal_weight_high = 24 * ((latest_report.user.info.height/100) ** 2)
    at_risk_weight_high = 25 * ((latest_report.user.info.height/100) ** 2)
    at_risk_weight_low = 18 * ((latest_report.user.info.height/100) ** 2)

    return render(request,
                  'health_adv_app/user_home.html',
                  context={'report_set': report_set,
                            'latest_report': latest_report,
                            'ideal_weight_low': int(ideal_weight_low),
                            'ideal_weight_high': int(ideal_weight_high),
                            'at_risk_weight_low': int(at_risk_weight_low),
                            'at_risk_weight_high': int(at_risk_weight_high),
                            'int_bmi': int(latest_report.bmi),},)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ideal_weight_low = 19 * ((context['report'].user.info.height/100) ** 2)
        ideal_weight_high = 24 * ((context['report'].user.info.height/100) ** 2)
        at_risk_weight_high = 25 * ((context['report'].user.info.height/100) ** 2)
        at_risk_weight_low = 18 * ((context['report'].user.info.height/100) ** 2)

        context['latest_report'] = context['report']
        context['ideal_weight_low'] = int(ideal_weight_low)
        context['ideal_weight_high'] = int(ideal_weight_high)
        context['at_risk_weight_low'] = int(at_risk_weight_low)
        context['at_risk_weight_high'] = int(at_risk_weight_high)
        context['int_bmi'] = int(context['report'].bmi)

        return context


class DeleteReportView(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy("health_adv_app:user_home")
