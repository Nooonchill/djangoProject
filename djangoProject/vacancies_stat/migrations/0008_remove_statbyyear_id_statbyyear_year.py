# Generated by Django 4.1.3 on 2024-01-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_stat', '0007_statbyyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statbyyear',
            name='id',
        ),
        migrations.AddField(
            model_name='statbyyear',
            name='year',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Год'),
        ),
    ]
