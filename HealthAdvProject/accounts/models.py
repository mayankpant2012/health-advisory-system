from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,
                                on_delete='CASCADE',
                                related_name='info',)

    # Add any additional attributes you want
    dob = models.DateField()
    age =  models.PositiveSmallIntegerField()
    GENDER_CHOICES = (
        (0, 'Female'),
        (1, 'Male'),
    )

    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    height = models.PositiveSmallIntegerField()

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
