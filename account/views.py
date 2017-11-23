from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from . import controllers
# Create your views here.


def logout(request):
    return Http404


@login_required(login_url="/accounts/login")
def index(request):
    user = request.user
    newsList= controllers.find_latest_news
    courseList= controllers.find_valid_course
    taskList = controllers.find_valid_task

    context = {
        "user": user.get_username(),
        "time": timezone.now(),
        "newsList": newsList,
        "courseList": courseList,
        "taskList": taskList,
    }

    return render_to_response("index.html", context)
