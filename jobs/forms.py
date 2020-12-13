from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse

from jobs.models import Company, Vacancy, Specialty


class ApplicationForm(forms.Form):
    written_username = forms.CharField(max_length=100, label='Имя', error_messages={'required': 'Введите свое имя!'})
    written_phone = forms.IntegerField(label='Номер телефона', error_messages={'required': 'Введите номер телефона!'})
    written_cover_letter = forms.CharField(label='Сопроводительное письмо:', error_messages={'required':'Напишите сопроводительное письмо.'})


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max')

