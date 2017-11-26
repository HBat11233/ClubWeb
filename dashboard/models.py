from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class News(models.Model):
    '''
    年轻人不要总想着大新闻
    '''
    newsTitle = models.CharField(max_length=50)
    newsContent = models.TextField(max_length=500)
    newsDate = models.DateField(default=datetime.now())

    def __str__(self):
        return self.newsTitle

    def get_absolute_url(self):
        return "news/{}".format(self.id)


class Task(models.Model):
    '''
    homework and task with deadline, for students
    '''
    taskName = models.CharField(max_length=50)
    taskContent = models.TextField(max_length=500)
    taskDeadline = models.DateTimeField()
    taskStudents = models.ManyToManyField(User)

    __visuable=['taskName','taskContent', 'taskDeadline']

    def __str__(self):
        return self.taskName

    def get_absolute_url(self):
        return "task/{}".format(self.id)

class Course(models.Model):
    '''
    course of club, one manager(teacher), many students
    '''
    courseName = models.CharField(max_length=50)
    courseContent = models.TextField(max_length=500)
    courseStart = models.DateTimeField()
    courseTime = models.CharField(max_length=20)
    coursePlace = models.CharField(max_length=50)
    courseStudents = models.ManyToManyField(User)


    __visuable=['courseName','courseContent', 'courseStart', 'courseTime', 'coursePlace']
    
    def __str__(self):
        return self.courseName

    def get_absolute_url(self):
        return "course/{}".format(self.id)

class Schedule(models.Model):
    '''
    todo list for managers
    '''
    scheduleName = models.CharField(max_length=50)
    scheduleContent = models.TextField(max_length=1000)
    scheduleDeadline = models.DateTimeField()

    def __str__(self):
        return self.scheduleName

    def get_absolute_url(self):
        return "schedule/{}".format(self.id)
