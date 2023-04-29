from django.db import models

# Create your models here.
class Schedule(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    schedule_date = models.DateTimeField()
    remind_date = models.IntegerField()
    isActive = models.BooleanField()
