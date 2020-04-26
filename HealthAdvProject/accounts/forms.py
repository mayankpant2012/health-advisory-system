from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models
from django.forms.widgets import SelectDateWidget


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
    year_list = [x for x in range(2020,1930,-1)]
    dob = forms.DateField(label='Date of Birth',
                          widget=SelectDateWidget(years=year_list))
    class Meta:
        model = models.UserProfileInfo
        fields = ['dob',
                  'gender',
                  'weight',
                  'height',
                  'chest_pain',
                  'age',
                  'glucose',
                  'cholestrol',
                  'systolic_bp',
                  'diastolic_bp',
                  ]
