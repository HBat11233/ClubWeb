from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Task)
admin.site.register(models.News)
admin.site.register(models.Schedule)