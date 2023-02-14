from django.contrib import admin
from . import models

@admin.register(models.Submissions)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'submissiontitle',
        'submitted',
        'submitter',
        'assignment'
    ]
# Register your models here.
