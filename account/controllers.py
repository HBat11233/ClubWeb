from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime


def find_latest_news(valid_days=7):
    valid_date = datetime.datetime.now().date() - datetime.timedelta(days=valid_days)
    latest_news = News.objects.filter(newsDate__gt=valid_date)
    if latest_news:
        return [NewsForm(instance=news) for news in latest_news]


def find_valid_task(user):
    now_time = datetime.datetime.now()
    valid_task = user.task_set.filter(taskDeadline__lt=now_time)
    if valid_task:
        return [TaskForm(instance=task) for task in valid_task]

def find_valid_course(user):
    now_time = datetime.datetime.now()
    valid_course = user.course_set.filter(courseStart__lt=now_time)
    if valid_course:
        return [CourseForm(instance=course) for course in valid_course]