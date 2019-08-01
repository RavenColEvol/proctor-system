from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Department)
admin.site.register(models.Proctor)
admin.site.register(models.Student)