from django.contrib import admin
from .models import Teacher, Student, Subject, Person, Exam

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["get_name",]
    def get_name(self, obj):
        return obj.details.name

class ExamAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name",]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["get_name",]
    def get_name(self, obj):
        return obj.details.name

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Exam, ExamAdmin)
