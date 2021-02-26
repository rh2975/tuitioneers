from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    pic = models.ImageField(default="ttnapp/static/img/uploads/368-kakashi.png", upload_to="uploads/", blank=True)
    details = models.CharField(max_length=1000, blank=True)
    fb = models.CharField(max_length=100, blank=True)
    insta = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)


class Teacher(models.Model):
    dept = models.CharField(max_length=100)
    details = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="teacher_details")


class Student(models.Model):
    details = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="student_details")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="student_teacher")


class Subject(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="taken_subjects")

class Exam(models.Model):
    name = models.CharField(max_length=200)
    obtained_marks = models.IntegerField(default=0)
    fullmarks = models.IntegerField(default=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_exam")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_exam")
