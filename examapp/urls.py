from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fill-exam-form/', views.fill_exam_form, name='fill_exam_form'),
    path('submission-success/', views.submission_success, name='submission_success'),
]
