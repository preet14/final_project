from django.db import models
from Details.models import *
from instructor.models import *


# Create your models here.
class Student(models.Model):
    regId = models.CharField(max_length=10)
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20, null=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=12, null=True)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email
