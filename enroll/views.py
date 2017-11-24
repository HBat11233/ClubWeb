from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import EnrollmentForm


# Create your views here.


class register(View):
    def post(self, request):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollInfo = form.save()
            user = User.objects.create_user(
                username=enrollInfo.enrollCode, password=None)
            user.save()
            enrollInfo.enrollUser = user
            enrollInfo.save()
            return HttpResponseRedirect('/enroll/thanks/')
        else:
            return HttpResponseRedirect('/enroll/sorry/')

    def get(self, request):
        context = {"form": EnrollmentForm()}
        context.update(csrf(request))
        return render(request, 'enroll.html', context)


# class register(FormView):
#     template_name = 'enroll.html'
#     form_class = EnrollmentForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         enrollInfo = form.save()
#         enrollInfo.save()
#         return HttpResponseRedirect('/enroll/thanks/')


def thanks(request):
    return render_to_response('thanks.html')


def sorry(request):
    return render_to_response('sorry.html')
