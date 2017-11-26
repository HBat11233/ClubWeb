from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
    url(r'^$', csrf_protect(views.register.as_view()), name='register'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^sorry/$', views.sorry, name='sorry'),
]