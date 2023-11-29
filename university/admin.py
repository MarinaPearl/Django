from django.contrib import admin
from .models import UniversityModel, StudentModel


class StudentAdmin(admin.ModelAdmin):
    # Данная переменная указывает на поля, которые будут выводится в списке продуктов
    list_display = ('full_name', 'date_of_birth', 'university', 'year_admission')


admin.site.register(StudentModel, StudentAdmin)


class UniversityAdmin(admin.ModelAdmin):
    # Данная переменная указывает на поля, которые будут выводится в списке продуктов
    list_display = ('name', 'abbreviated', 'data_creation',)


admin.site.register(UniversityModel, UniversityAdmin)
