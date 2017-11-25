from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from enroll.models import Enrollment
from django.contrib.auth.models import User
# Create your views here.


def profile(request):
    ''''''


    template_name = 'profile.html'
    user = request.user
    enrollInfo = Enrollment.objects.filter(enrollUser=request.user.id)
    context = {'profile:': enrollInfo, 'user': user}
    return render_to_response(template_name, context)
