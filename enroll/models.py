from django.db import models

# Create your models here.


class enrollment(models.Model):
    experience_choice = [
        (0, 'Freshman to programming'),
        (1, 'Some experiences in one or more languages'),
        (2, 'Experienced developer'),
        (3, 'Unavailable')
    ]
    gender_choice = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    enrollCode = models.CharField(
        max_length=10, primary_key=True, unique=True)
    enrollName = models.CharField(max_length=20)
    enrollGender = models.CharField(max_length=1, choices=gender_choice, default='M')
    enrollCollege = models.CharField(max_length=30)
    enrollEmail = models.EmailField(max_length=100)
    enrollIntro = models.IntegerField(choices=experience_choice, default=0)
    interviewScoreOne = models.IntegerField(default=0, null=True)
    interviewScoreTwo = models.IntegerField(default=0, null=True)
    examScore = models.IntegerField(default=0, null=True)
    isPassed = models.BooleanField(default=False)
    


    def __str__(self):
        return "{0}: {1}".format(self.enrollCode, self.enrollName)
