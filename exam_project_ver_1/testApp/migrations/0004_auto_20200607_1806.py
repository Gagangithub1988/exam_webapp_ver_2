# Generated by Django 3.0.5 on 2020-06-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_auto_20200607_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contact_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
