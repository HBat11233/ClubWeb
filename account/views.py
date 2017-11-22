from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from .forms import *
# Create your views here.


def logout(request):
    return Http404


@login_required(login_url="/accounts/login")
def index(request):
    user = request.user

    context = {
        "user": user.get_username(),
        "time": now(),
        "news": NewsForm,
        "course_form": CourseForm,
        "deadline": TaskForm,
    }

    return render_to_response("index.html", context)
