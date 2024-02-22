from django.db import models

# Create your models here.

class Courier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    xcoordination = models.CharField(max_length=255, default=None, null=True)
    ycoordination = models.CharField(max_length=255, default=None, null=True)
