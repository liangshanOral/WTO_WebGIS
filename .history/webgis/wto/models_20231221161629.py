from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=3, unique=True)  # If a code is available
    name = models.CharField(max_length=100, unique=True)
