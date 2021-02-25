from django.contrib import admin
from .models import Teacher, Student, Subject, Person, Exam

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Person, PersonAdmin)
admin.site.register(Exam)
