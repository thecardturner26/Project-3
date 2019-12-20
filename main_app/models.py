from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=60)
  d_o_b = models.DateField()
  user_relation = models.CharField(max_length=30)
  healthcare = models.CharField(max_length=50)
  pills = models.ManyToManyField(Pills)
  appointments = models.ManyToManyField(Appointments)
  
  def __str__(self):
      return self.name
  

    
patients = [
    Patient('Zach', 8132001, 'Back-Man', 'Arkids', [{'name': 'Witch Doctor', 'date': '2019-12-19 17:17:24.943901', 'practioner': 'Nazeebo', 'location': 'Congress Ave, Austin, TX 78704', 'note' : ''}] ,[{'name': 'Joy', 'total': 14, 'days': {'monday': ['0800','0800'], 'tuesday':[''],'wednesday': ['0800'],'thursday': [''],'friday': [''],'saturday': [''],'sunday': ['']}, 'dosage': 3}] ),
    Patient('Marco', 1122000, 'Midle-Man', 'MarcoCare', [], []),
    Patient('Juan', 1011970, 'Front-Man', 'MarcoCare', [] , [])
]

class Pills(models.Model):
    name = models.CharField(max_length=80)
    total = models.IntegerField()
    days = models.ManyToManyField(Days)
    dosage = models.IntegerField()

    def __init__(self, name, total, days, times, dosage):
        
        
class Days(models.Model):
     monday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     tuesday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     wednesday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     thursday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     friday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     saturday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     sunday = models.ArrayField(
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none),
         models.TimeField(default=none)
     )
     def __str__(self):
        return self
        
class Appointment:
    name = models.CharField()
    date = models.DateField()
    practioner = models.CharField()
    location = models.CharField()
    note = models.TextField()