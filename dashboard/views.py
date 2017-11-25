from django.shortcuts import render, render_to_response, Http404, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.utils import timezone
from .models import *
# Create your views here.


@login_required(login_url="/accounts/login")
def dashboard(request):

    def find_latest_news(valid_days=7):
        valid_date = datetime.datetime.now().date() - datetime.timedelta(days=valid_days)
        latest_news = News.objects.filter(newsDate__gt=valid_date)
        if latest_news:
            return latest_news

    def find_valid_task(user):
        now_time = datetime.datetime.now()
        valid_task = user.task_set.filter(taskDeadline__lt=now_time)
        if valid_task:
            return valid_task

    def find_valid_course(user):
        now_time = datetime.datetime.now()
        valid_course = user.course_set.filter(courseStart__lt=now_time)
        if valid_course:
            return valid_course

    user = request.user
    newsList = find_latest_news()
    courseList = controllers.find_valid_course(user)
    taskList = controllers.find_valid_task(user)

    context = {
        "user": user.get_username(),
        "time": timezone.now(),
        "newsList": newsList,
        "courseList": courseList,
        "taskList": taskList,
    }

    return render_to_response("dashboard.html", context)


def news_detail_view(request, pk):
    news_id = get_object_or_404(News, pk=pk)

    return render(
        request,
        'news_detail.html',
        context={'news': news_id, }
    )


def task_detail_view(request, pk):
    task_id = get_object_or_404(Task, pk=pk)

    return render(
        request,
        'task_detail.html',
        context={'task': task_id, }
    )


def course_detail_view(request, pk):
    course_id = get_object_or_404(Course, pk=pk)

    return render(
        request,
        'course_detail.html',
        context={'course': course_id, }
    )

