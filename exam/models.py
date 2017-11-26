from django.db import models
from django.contrib.auth.models import User
from enroll.models import Enrollment
from datetime import datetime, timedelta

# Create your models here.
class SingleChoice(models.Model):
    choice=[
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D')
    ]

    content=models.TextField(max_length=500)
    correctAnswer=models.IntegerField(choices=choice,default=1)
    score=models.IntegerField(default=2)

    A=models.CharField(max_length=100)
    B=models.CharField(max_length=100)
    C=models.CharField(max_length=100)
    D=models.CharField(max_length=100)

    def __str__(self):
        return '{0}: {1}'.format(id, self.content[:10])


class ShortAnswer(models.Model): 
    briefIntro=models.CharField(max_length=30)
    content=models.TextField(max_length=800)
    score=models.IntegerField(default=10)



class TestPaper(models.Model):
    singleChoices=models.ManyToManyField(SingleChoice)
    shortAnswers=models.ManyToManyField(ShortAnswer)


class Exam(models.Model):
    student=models.OneToOneField(User)
    paper=models.OneToOneField(TestPaper)
    score=models.IntegerField(null=True)

    startTime=models.TimeField(null=True)
    endTime=models.TimeField(null=True)
    timeLimit=models.Field(default=timedelta(seconds=1200))

    def template_mapper(self):
        ''' '''
        pass
    #     paper=self.paper

    #     for choice in paper.singleChoices:
            
    #     for answer in paper.shortAnswers:

    def is_valid(self):
        if self.startTime:
            if self.endTime:
                return self.endTime-self.startTime<self.timeLimit
        return False