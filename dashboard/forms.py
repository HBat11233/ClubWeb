from .models import Course, Task, News, Schedule
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName','taskContent', 'taskDeadline']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['courseName','courseContent', 'courseStart', 'courseTime', 'coursePlace']
