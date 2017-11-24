from django.shortcuts import render, render_to_response, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.detail import DetailView
from enroll.models import Enrollment
from django.contrib.auth.models import User
# Create your views here.


class profile(DetailView):
    model = Enrollment
    template_name = 'profile.html'
    queryset = Enrollment.objects.filter(enrollUser=self.request.user.id)

