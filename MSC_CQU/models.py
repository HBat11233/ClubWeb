from django.db import models
from django.contrib.auth.models import UserManager
import datetime

class news(models.Model):
    content=models.TextField(max_length=1000)
    pub_date=models.DateField(default=datetime.datetime.now())

class task(models.Model):
    task=models.TextField(max_length=300)
    deadline=models.DateTimeField()

class course(models.Model):
    time_start=models.DateTimeField()
    time_need=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    speaker=models.ForeignKey(UserManager)