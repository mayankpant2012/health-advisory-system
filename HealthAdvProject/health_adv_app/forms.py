from django import forms
from . import models

class ReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        exclude = ['user',
                   'bmi',
                   'generation_date',
                   'fbs',
                   'heart_disease',
                   'slope',
                   'ca',
                   'thal',
                   'heart_disease',
                   'diabetes',
                   'stroke',
                   ]



#HELP
'''
from django.utils.translation import gettext_lazy as _  #used for translation

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
'''
