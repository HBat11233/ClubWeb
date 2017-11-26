from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from enroll.models import Enrollment
from django.template.context_processors import csrf
import time

# Create your views here.


def profile(request):
    ''''''

    template_name = 'profile.html'
    user = request.user
    context = {'user': user}
    return render_to_response(template_name, context)


class PasswordReset(View):
    template_name = 'password.html'

    def get(self, request):
        form = PasswordChangeForm(request.user)
        context={'get': True, 'form': form}
        context.update(csrf(request))
        return render_to_response(self.template_name, context)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render_to_response(self.template_name, {'success': True})
        else:
            return render_to_response(self.template_name, {'success': False})
