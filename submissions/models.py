from django.db import models
from users.models import ExtendUser
from assignments.models import Assignments
from django.utils.translation import gettext_lazy as _


class Submissions(models.Model):
    submissiontitle = models.CharField(max_length=250, default=_("New Submission"))
    submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(ExtendUser, default=1, on_delete=models.DO_NOTHING, verbose_name="Submitter")
    assignment = models.ForeignKey(Assignments, default=1, on_delete=models.CASCADE, verbose_name="Assignment")

  

    def __str__(self):
        return self.submissiontitle
# Create your models here.
