from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
# Create your views here.

def logout(request):
    return Http404

@login_required(login_url="/accounts/login")
def index(request):
    return render_to_response("index.html",{"user": request.user.get_username(),"time":datetime.datetime.now()})
