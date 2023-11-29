from django import forms
from django.forms import widgets

from university.models import UniversityModel


class UniversityForm(forms.Form):
    name = forms.CharField(label='Название университета')
    abbreviated = forms.CharField(label='Короткое название университета')
    date_creation = forms.DateField(
        label='Дата создания', widget=widgets.DateInput(attrs={'type': 'date'})
    )


class StudentForm(forms.Form):
    full_name = forms.CharField(label='ФИО')
    date_of_birth = forms.DateField(label='День Рождения', widget=widgets.DateInput(attrs={'type': 'date'}))
    university = forms.ModelChoiceField(label='Университет', queryset=UniversityModel.objects.all(),
                                        to_field_name='abbreviated')
    year_admission = forms.DateField(label='Год поступления', widget=widgets.DateInput(attrs={'type': 'date'}))
