from django.contrib import admin
from .models import (
    User,
    Department,
    Proctor,
    Student,
    Messages
)
# Register your models here.

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Proctor)
admin.site.register(Student)
admin.site.register(Messages)