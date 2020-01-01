# Generated by Django 3.0.1 on 2019-12-20 21:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('practioner', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=100)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('tuesday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('wednesday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('thursday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('friday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('saturday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
                ('sunday', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=4), size=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('total', models.IntegerField()),
                ('dosage', models.IntegerField()),
                ('days', models.ManyToManyField(to='main_app.Days')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('d_o_b', models.DateField()),
                ('user_relation', models.CharField(max_length=30)),
                ('healthcare', models.CharField(max_length=50)),
                ('appointments', models.ManyToManyField(to='main_app.Appointments')),
                ('pills', models.ManyToManyField(to='main_app.Pills')),
            ],
        ),
    ]
