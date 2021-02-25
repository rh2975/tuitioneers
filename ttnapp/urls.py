from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/<int:teacher_id>/', views.teacher, name='teacher'),
    path('student/<int:student_id>/', views.student, name='student'),
    path('student/<int:student_id>/<int:subject_id>', views.subject_exams, name='subject_exams'),
    path('student/<int:student_id>/<int:subject_id>/<int:exam_id>', views.subject_marks, name='subject_marks'),
]
