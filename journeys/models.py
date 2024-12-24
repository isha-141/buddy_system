from django.db import models

# Create your models here.
class Journey(models.Model):
    PID = models.IntegerField(null=True)
    fullname = models.CharField(max_length=255)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    start_time = models.TimeField(null=True)