from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import EnrollmentForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollInfo = form.save()
            enrollInfo.save()
            return HttpResponseRedirect('/enroll/thanks/') 
        else:
            return HttpResponseRedirect('/enroll/sorry/')
    else:
        context = {"form": EnrollmentForm()}
        context.update(csrf(request))
        return render(request, 'enroll.html', context)

def thanks(request):
    return render_to_response('thanks.html')

def sorry(request):
    return render_to_response('sorry.html')
