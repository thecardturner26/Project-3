from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Days(models.Model):
  name = models.CharField(max_length=5, default='')
  monday = ArrayField(
      ArrayField(
        models.CharField(max_length=5),
        size=4
  ),
    size=4
  )
  tuesday = ArrayField(
      ArrayField(
        models.CharField(default='20:00' , max_length=5),
        size=4
  ),
    size=4
  )
  wednesday = ArrayField(
      ArrayField(
         models.CharField(default='20:00', max_length=5),
        size=4
  ),
    size=4
  )
  thursday = ArrayField(
      ArrayField(
        models.CharField(default='20:00', max_length=5),
        size=4
  ),
    size=4
  )
  friday = ArrayField(
      ArrayField(
        models.CharField(default='20:00', max_length=5),
        size=4
  ),
    size=4
  )
  saturday = ArrayField(
      ArrayField(
        models.CharField(default='20:00', max_length=5),
        size=4
  ),
    size=4
  )
  sunday = ArrayField(
      ArrayField(
        models.CharField(default='20:00', max_length=5),
        size=4
  ),
    size=4
  )
  
  def __arry__(self):
    return self.name


class Pills(models.Model):
  name = models.CharField(max_length=80)
  total = models.IntegerField()
  pil_days = models.ManyToManyField(Days)
  dosage = models.IntegerField()
  def __str__(self):
    return self.name

class Appointments(models.Model):
  name = models.CharField(max_length=60)
  app_date = models.DateField()
  practioner = models.CharField(max_length=60)
  location = models.CharField(max_length=100)
  note = models.TextField()
  def __str__(self):
    return self.name

class Patient(models.Model):
  name = models.CharField(max_length=60)
  d_o_b = models.DateField()
  user_relation = models.CharField(max_length=30)
  healthcare = models.CharField(max_length=50)
  pills = models.ManyToManyField(Pills)
  appointments = models.ManyToManyField(Appointments)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  
