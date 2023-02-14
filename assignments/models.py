from django.db import models
from users.models import ExtendUser
from courses.models import Courses
from django.utils.translation import gettext_lazy as _

class Assignments(models.Model):
    assignmenttitle = models.CharField(max_length=250, default=_("New Assignment"))
    submitted = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(ExtendUser, default=1, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Courses, default=1,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.assignmenttitle
    
# Create your models here.
