# Generated by Django 3.0.5 on 2020-06-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20200606_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
