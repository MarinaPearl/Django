from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    # path('', views.university_home, name='university_home'),
    path('create_university', views.create_university, name='create_university'),
    path('create_student', views.create_student, name='create_student'),
    path('universities', views.universities, name='universities'),
    path('update_university/<int:university_id>', views.update_university, name='update_university'),
    path('remove_university/<int:university_id>', views.remove_university, name='remove_university'),

    path('students', views.students, name='students'),
    path('update_student/<int:student_id>', views.update_student, name='update_student'),
    path('remove_student/<int:student_id>', views.remove_student, name='remove_student'),
]
