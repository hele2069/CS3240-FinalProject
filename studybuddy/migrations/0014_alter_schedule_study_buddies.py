# Generated by Django 3.2.13 on 2022-05-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0013_auto_20220503_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='study_buddies',
            field=models.ManyToManyField(default=None, to='studybuddy.Profile'),
        ),
    ]