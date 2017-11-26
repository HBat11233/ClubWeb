from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View


def home(request):
    return render_to_response('home.html')

