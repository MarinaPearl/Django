from django.db import models


class UniversityModel(models.Model):
    name = models.CharField('Полное название', max_length=250)
    abbreviated = models.CharField('Сокращенное название', max_length=250, unique=True)
    data_creation = models.DateField('Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'


class StudentModel(models.Model):
    full_name = models.CharField('ФИО', max_length=250)
    date_of_birth = models.DateField('Дата рождения')
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE, null=True)
    year_admission = models.DateField('Год поступления')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
