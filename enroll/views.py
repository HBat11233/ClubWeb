from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.views import View
from .forms import EnrollmentForm


# Create your views here.


class register(View):
    def post(self, request):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollInfo = form.save()
            if request.user.is_authenticated:
                user = request.user
            else:
                user = User.objects.create_user(
                    username=enrollInfo.enrollEmail, password=enrollInfo.enrollCode)
                user.save()
            enrollInfo.enrollUser = user
            enrollInfo.save()
            return HttpResponseRedirect('/enroll/thanks/')
        else:
            return HttpResponseRedirect('/enroll/sorry/')

    def get(self, request):
        if request.user.is_authenticated():
            if request.user.enrollment:
                return render_to_response("sorry.html",context={'user':request.user})
        context = {"form": EnrollmentForm()}
        context.update(csrf(request))
        return render_to_response('enroll.html', context)


def thanks(request):
    return render_to_response('thanks.html')


def sorry(request):
    return render_to_response('sorry.html')
