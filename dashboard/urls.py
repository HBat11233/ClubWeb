from django.conf.urls import url
from . import views
# Create your tests here.

urlpatterns = [
    url(r'^$', views.dashboard, name='register'),
    url(r'^news/(?P<pk>[0-9]+)/$',
        views.news_detail_view, name='news_detail'),
    url(r'^task/(?P<pk>[0-9]+)/$',
        TaskDetailView.as_view(), name='task_detail'),
    url(r'^course/(?P<pk>[0-9]+)/$',
        CourseDetailView.as_view(), name='course_detail'),
]
