from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Student)


@admin.register(Student)
class HeroStudent(admin.ModelAdmin):
    list_display = ("user", "regId", "active", "contact", "course", "instructor", "batch")
    actions = ["activate_student", "deactivate_student"]

    def activate_student(self, request, queryset):
        queryset.update(active=True)

    def deactivate_student(self, request, queryset):
        queryset.update(active=False)
