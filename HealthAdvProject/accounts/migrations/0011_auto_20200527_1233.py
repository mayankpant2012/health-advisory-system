# Generated by Django 2.2.7 on 2020-05-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200503_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
