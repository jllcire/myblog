# Generated by Django 3.1.2 on 2021-02-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=32)),
                ('continent', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('total_cases', models.IntegerField()),
                ('new_cases', models.IntegerField()),
                ('new_cases_smoothed', models.FloatField()),
                ('total_deaths', models.IntegerField()),
                ('new_deaths', models.IntegerField()),
                ('new_deaths_smoothed', models.FloatField()),
            ],
        ),
    ]