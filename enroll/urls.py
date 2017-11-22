from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    url('^register/', CreateView.as_view(
        template_name='enroll.html',
        form_class=UserCreationForm,
        success_url='/'
    )),
    url(r'^$', views.register, name='register'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^sorry/$', views.sorry, name='sorry'),
]