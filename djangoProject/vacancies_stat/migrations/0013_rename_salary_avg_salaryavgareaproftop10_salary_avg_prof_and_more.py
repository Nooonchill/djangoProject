# Generated by Django 4.1.3 on 2024-01-20 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies_stat', '0012_salaryavgareaproftop10_salaryavgareatop10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salaryavgareaproftop10',
            old_name='salary_avg',
            new_name='salary_avg_prof',
        ),
        migrations.RenameField(
            model_name='vacanciespercentareaproftop10',
            old_name='vacancies_percent',
            new_name='vacancies_percent_prof',
        ),
    ]
