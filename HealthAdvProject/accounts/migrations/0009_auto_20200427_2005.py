# Generated by Django 2.2.7 on 2020-04-27 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200117_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='chest_pain',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='cholestrol',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='diastolic_bp',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='glucose',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='systolic_bp',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='weight',
        ),
    ]
