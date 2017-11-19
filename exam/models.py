from django.db import models
from enroll.models import enrollment

# Create your models here.
class single_choice(models.Model):
    choice=[
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D')
    ]

    description=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    correct_answer=models.IntegerField(choices=choice,default=1)

    A=models.CharField(max_length=100)
    B=models.CharField(max_length=100)
    C=models.CharField(max_length=100)
    D=models.CharField(max_length=100)

    def __str__(self):
        return '{0}: {1}'.format(id,self.description)


class exam(models.Model):
    pub_date=models.DateField()
    start_time=models.TimeField()
    student=models.OneToOneField(enrollment, on_delete=models.CASCADE)
    single_choices=models.ManyToManyField(single_choice)