# Generated by Django 3.0.5 on 2020-04-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_basic', '0002_auto_20200429_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
