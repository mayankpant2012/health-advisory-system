from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

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
                   'glucose_plot',
                   'weight_plot',
                   'cholestrol_plot',
                   'bp_plot',
                   ]
        labels = {
            'glucose': _('Blood Sugar'),
            'cholestrol': _('Total Cholestrol'),
            'systolic_bp': _('Systolic Blood Pressure'),
            'diastolic_bp': _('Diastolic Blood Pressure'),
            'hypertension': _('Do you have hypertension?'),
            'exang': _('Do you experience chest pain during exercising?'),
            'chest_pain': _('Do you experience chest pain in your day to day life?')
        }


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
