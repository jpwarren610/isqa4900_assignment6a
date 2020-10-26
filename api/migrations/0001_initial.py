# Generated by Django 3.0.7 on 2020-10-26 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_location', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('meat', models.CharField(max_length=100)),
                ('injection', models.CharField(max_length=100)),
                ('rub', models.CharField(max_length=100)),
                ('pit', models.CharField(max_length=100)),
                ('fuel', models.CharField(max_length=100)),
                ('pit_temp', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('final_temp', models.IntegerField()),
                ('judge_score', models.IntegerField()),
                ('notes', models.TextField(max_length=360)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]