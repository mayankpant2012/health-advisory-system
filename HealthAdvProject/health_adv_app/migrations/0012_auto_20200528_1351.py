# Generated by Django 2.2.7 on 2020-05-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_adv_app', '0011_auto_20200528_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='generation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
