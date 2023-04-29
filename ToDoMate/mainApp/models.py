from django.db import models

# Create your models here.
class Schedule(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    month = models.IntegerField(null=False,default=4)
    day = models.IntegerField(null=False,default=10)
    remind_date = models.IntegerField()
    is_active = models.BooleanField()
