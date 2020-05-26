from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from . import predictors
from datetime import date

class Report(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.ForeignKey(User, on_delete='CASCADE')

    CHEST_PAIN_CHOICES = (
        (0, 'None'),
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'Severe'),
    )

    HYPERTENSION_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )

    REST_ECG_CHOICES = (
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High'),
    )

    EXANG_CHOICES = (
        (0, 'No'),
        (1, 'Yes'),
    )

    RESIDENCE_TYPE_CHOICES = (
        (0, 'Rural'),
        (1, 'Urban'),
    )

    #INPUT ATTRIBUTES
    weight = models.PositiveSmallIntegerField()
    bmi = models.FloatField(blank=True, null=True)
    glucose = models.PositiveSmallIntegerField(default=0)
    cholestrol = models.FloatField(default=0)
    pregnancies = models.PositiveSmallIntegerField(default=0)#dont show in form if sex is male i.e. 1
    skin_thickness = models.PositiveSmallIntegerField(default=0)
    systolic_bp = models.PositiveSmallIntegerField(default=0)
    diastolic_bp = models.PositiveSmallIntegerField(default=0)
    hypertension = models.PositiveSmallIntegerField(choices=HYPERTENSION_CHOICES,
                                                    default=0)
    chest_pain = models.PositiveSmallIntegerField(choices=CHEST_PAIN_CHOICES,
                                                  default=0)
    generation_date = models.DateField(default=timezone.now)
    
    #exercise induced angina:
    #Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood.
    exang = models.PositiveSmallIntegerField(choices = EXANG_CHOICES,
                                             default=0)

    #fasting blood sugar
    #whether fasting blod sugar is > 120, 0 means < 120
    fbs = models.PositiveSmallIntegerField(default=0)

    #Restecg - resting electrocardiographic results (values 0,1,2)
    rest_ecg = models.PositiveSmallIntegerField(choices=REST_ECG_CHOICES,
                                                default=0)
    residence_type = models.PositiveSmallIntegerField(choices=RESIDENCE_TYPE_CHOICES,
                                                      default=0)#0 means rural


    #DEFAULTS
    slope = models.PositiveSmallIntegerField(default=0)
    ca = models.PositiveSmallIntegerField(default=0)
    thal = models.PositiveSmallIntegerField(default=0)


    #OUTPUTS
    heart_disease = models.PositiveSmallIntegerField(default=0,blank=True, null=True)
    diabetes = models.PositiveSmallIntegerField(blank=True, null=True)
    stroke = models.PositiveSmallIntegerField(blank=True, null=True)


    #META class
    class Meta:
        ordering = ['-generation_date']


    #METHODS
    def calculate_fbs(self):
        if self.glucose >= 120:
            self.fbs = 1
        self.save()

    def calculate_bmi(self):
        weight = self.weight
        height_sq = (self.user.info.height/100)**2
        bmi = weight/height_sq
        self.bmi = bmi
        self.save()

    def calculate_age(self):
        today = date.today()
        born = self.user.info.dob
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        self.user.info.age = age
        self.user.info.save()

    def calculate_heart_disease(self):
        input_list = [self.user.info.age,
                      self.user.info.gender,
                      self.systolic_bp,
                      self.cholestrol,
                      self.fbs,
                      self.exang,
                      self.chest_pain,
                      self.rest_ecg,]
        self.heart_disease = predictors.heart_disease_predictor(input_list)
        self.save()

    def calculate_diabetes(self):
        input_list = [self.pregnancies,
                      self.glucose,
                      self.diastolic_bp,
                      self.skin_thickness,
                      self.bmi,
                      self.user.info.age]
        self.diabetes = predictors.diabetes_predictor(input_list)
        self.save()

    def calculate_stroke(self):
        input_list = [self.user.info.age,
                      self.hypertension,
                      self.heart_disease,
                      self.bmi,
                      self.residence_type,
                      self.user.info.gender]
        self.stroke = predictors.stroke_predictor(input_list)
        self.save()

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.generation_date.strftime('%d %b %Y')
