# Generated by Django 2.2.7 on 2020-05-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_adv_app', '0012_auto_20200528_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='bp_plot',
            field=models.ImageField(blank=True, upload_to='images/plots/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='cholestrol_plot',
            field=models.ImageField(blank=True, upload_to='images/plots/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='weight_plot',
            field=models.ImageField(blank=True, upload_to='images/plots/'),
        ),
    ]
