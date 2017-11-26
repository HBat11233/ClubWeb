from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, password_change
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.profile), name='profile'),
    url(r'^login/$', LoginView.as_view(template_name="login.html", extra_context={"next": "/dashboard"})),
    url(r'^logout/$', LogoutView.as_view(template_name="logout.html")),
    #url(r'^chenge_profile/$',views.change_profile, name='change_profile')
    url(r'^password_reset/$', login_required(views.PasswordReset.as_view()),name='password_reset')
]
