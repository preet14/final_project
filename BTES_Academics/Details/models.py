from django.db import models


# Create your models here.
class Course(models.Model):
    courseId = models.CharField(max_length=20)
    courseName = models.CharField(max_length=20)

    def __str__(self):
        return self.courseName


class Batch(models.Model):
    batchName = models.CharField(max_length=20)
    bTime = models.DateTimeField()
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.batchName
