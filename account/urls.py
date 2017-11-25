from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.profile), name='profile'),
    url(r'^login/$', LoginView.as_view(template_name="login.html", extra_context={"next": "/dashboard"})),
    url(r'^logout/$', LogoutView.as_view(template_name="logout.html")),
    url(r'^password_reset/$', PasswordChangeView.as_view())
]
