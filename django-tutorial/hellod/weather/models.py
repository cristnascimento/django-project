from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200)
    recorded_date = models.DateTimeField('date recorded')
