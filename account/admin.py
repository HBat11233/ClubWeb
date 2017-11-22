from . import models
from django.contrib import admin


admin.site.register(models.Course)
admin.site.register(models.Task)
admin.site.register(models.News)
admin.site.register(models.Schedule)