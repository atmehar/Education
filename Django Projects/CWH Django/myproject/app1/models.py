from os import name
from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)
    desc = models.TextField()
    date = models.DateField()
