from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^sorry/$', views.sorry, name='sorry'),
]