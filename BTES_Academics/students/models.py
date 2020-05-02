from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from Details.models import *
from instructor.models import *
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    regId = models.CharField(max_length=10)
    # uname = models.CharField(max_length=20)
    # pwd = models.CharField(max_length=20, null=True)
    # fname = models.CharField(max_length=20)
    # lname = models.CharField(max_length=20, null=True)
    # email = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=False)
    contact = models.CharField(max_length=12, null=True)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.SET_NULL)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance=None, created=None, **kwargs):
    #     if created:
    #         Student.objects.create(user=instance)

    def __str__(self):
        return self.regId
