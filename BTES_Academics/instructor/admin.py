from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Instructor)
admin.site.register(FileUpload)
admin.site.register(QuizUpload)
admin.site.register(Comment)
