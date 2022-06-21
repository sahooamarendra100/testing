from unicodedata import name
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    dept = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(max_length=50)
    lastmodified_datetime = models.DateTimeField(max_length=50)
    
    