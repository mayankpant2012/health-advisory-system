# Generated by Django 2.2.7 on 2020-05-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_adv_app', '0009_auto_20200528_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='generation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
