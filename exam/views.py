from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
# Create your views here.

def exam(request):
    return render_to_response("developing..")