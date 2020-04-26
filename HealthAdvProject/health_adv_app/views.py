from django.shortcuts import render
from accounts.forms import LoginForm, UserCreateForm
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
    return render(request, 'health_adv/first_page.html', context)


def thanks(request):
    return render(request,'accounts/thanks.html')

def about(request):
    return render(request,'health_adv/about_us.html')

def contact(request):
    return render(request,'health_adv/contact_us.html')

def test(request):
    return render(request, 'health_adv/test.html')
