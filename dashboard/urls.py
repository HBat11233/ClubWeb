from django.conf.urls import url
from . import views
# Create your tests here.

urlpatterns = [
    url(r'^$', views.dashboard, name='register'),
]