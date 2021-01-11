from django.db import models

# Create your models here.



class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    tc = models.CharField(max_length=11)
    gsm = models.CharField(max_length=10)