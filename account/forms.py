from .models import Course, Task, News, Schedule
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        name = News
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        name = Task
        fields = ['Task', 'deadline']


class ScheduleForm(forms.ModelForm):
    class Meta:
        name = Schedule
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        name = Course
        fields = ['content', 'time_start', 'time_need', 'place']
