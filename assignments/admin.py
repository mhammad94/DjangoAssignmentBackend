from django.contrib import admin
from . import models


@admin.register(models.Assignments)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'assignmenttitle',
        'submitted',
        'submitter',
        'course',
    ]
# Register your models here.
