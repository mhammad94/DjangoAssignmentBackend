from django.contrib import admin
from . import models


@admin.register(models.Courses)

class CourseAdmin(admin.ModelAdmin):
        list_display = [
        'coursetitle'
    ]

# Register your models here.
