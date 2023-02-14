from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Courses(models.Model):
    coursetitle = models.CharField(max_length=250, default=_("New Course"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coursetitle
