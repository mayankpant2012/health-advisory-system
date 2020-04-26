from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete='CASCADE')

    # Add any additional attributes you want
    dob = models.DateField()
    age =  models.PositiveSmallIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CHEST_PAIN_CHOICES = (
        (0, 'None'),
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'Severe'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    chest_pain = models.PositiveSmallIntegerField(choices=CHEST_PAIN_CHOICES,
                                                  default=1)
    glucose = models.PositiveSmallIntegerField(default=0)
    cholestrol = models.PositiveSmallIntegerField(default=0)
    systolic_bp = models.PositiveSmallIntegerField(default=0)
    diastolic_bp = models.PositiveSmallIntegerField(default=0)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
