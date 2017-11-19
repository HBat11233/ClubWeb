from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(template_name="login.html",extra_context={"next": "/accounts"})),
    #url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name="logout.html")),
]

