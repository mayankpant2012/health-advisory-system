from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from . import models

from django.forms.widgets import SelectDateWidget
import datetime


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email Address"


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "User Name "
        self.fields["password"].label = "Password "


class UserProfileInfoForm(forms.ModelForm):
    now = datetime.datetime.now()
    year_list = [x for x in range(now.year,1930,-1)]
    dob = forms.DateField(label='Date of Birth',
                          widget=SelectDateWidget(years=year_list))
    class Meta:
        model = models.UserProfileInfo
        fields = ['dob',
                  'gender',
                  'height',
                  'age',
                  ]
