from django.db import models
from Details.models import *


# Create your models here.
class Instructor(models.Model):
    instructorId = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    batch = models.ManyToManyField(Batch)

    def __str__(self):
        return self.uname
