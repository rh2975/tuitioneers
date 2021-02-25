from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Teacher, Student, Subject, Exam

def index(request):
    context = {
        "teachers": Teacher.objects.all(),
        "students": Student.objects.all()
    }
    return render(request, 'home.html', context)

def teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        students = Student.objects.filter(teacher__id=teacher_id)
    except Student.DoesNotExist:
        raise Http404("No students sorry :3")
    context = {
        "teacher": teacher,
        "students": students,
    }
    return render(request, "teacher_students.html", context)

def student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        subjects = Subject.objects.filter(student__id=student_id)
    except Student.DoesNotExist:
        raise Http404("No such student")
    context = {
        "student": student,
        "subjects": subjects,
    }
    return render(request, "student_subs.html", context)


def subject_exams(request, student_id, subject_id):
    e = True
    try:
        student = Student.objects.get(pk=student_id)
        subject = Subject.objects.get(pk=subject_id)
        exams = Exam.objects.filter(subject__id=subject_id, student__id=student_id)
        if exams.count() == 0:
            e = False
    except Student.DoesNotExist:
        raise Http404("No such student")
    except Subject.DoesNotExist:
        raise Http404("No such subject available")
    context = {
        "student": student,
        "subject": subject,
        "exams": exams,
        "e": e,
    }
    return render(request, "subject_exams.html", context)


def subject_marks(request, student_id, subject_id, exam_id):
    try:
        subject = Subject.objects.get(pk=subject_id)
        exam = Exam.objects.get(pk=exam_id)
    except Student.DoesNotExist:
        raise Http404("No subjects sorry :3")
    context = {
        "subject": subject,
        "exam": exam,
    }
    return render(request, "subject_marks.html", context)
