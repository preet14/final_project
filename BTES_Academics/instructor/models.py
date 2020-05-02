from django.db import models
from Details.models import *
from django.contrib.auth.models import User


# Create your models here.
class Instructor(models.Model):
    instructorId = models.CharField(max_length=20)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    # uname = models.CharField(max_length=20)
    # pwd = models.CharField(max_length=20)
    # email = models.CharField(max_length=50)
    # fname = models.CharField(max_length=20)
    # lname = models.CharField(max_length=20)
    type = models.BooleanField(default=True)
    contact = models.CharField(max_length=20)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    batch = models.ManyToManyField(Batch)

    def __str__(self):
        return self.instructorId


class FileUpload(models.Model):
    courseName = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    topic = models.CharField(max_length=20)
    content = models.TextField(max_length=5000)
    filename = models.CharField(max_length=500)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.topic


class QuizUpload(models.Model):
    courseName = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    topicName = models.ForeignKey(FileUpload, null=True, on_delete=models.CASCADE)
    Question = models.CharField(max_length=1000)
    optionA = models.CharField(max_length=250)
    optionB = models.CharField(max_length=250)
    optionC = models.CharField(max_length=250)
    optionD = models.CharField(max_length=250)
    correctOption = models.CharField(max_length=250)
    explanation = models.TextField(max_length=250)

    def __str__(self):
        return self.topicName.topic + ' : ' + str(self.Question)


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.course.courseName, str(self.user.username))
