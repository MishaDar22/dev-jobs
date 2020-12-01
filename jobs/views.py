from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.views import View

from jobs.models import Specialty, Company, Vacancy


def custom_handler404(request, exception):
    return HttpResponseNotFound('Что-то сломалось :(')


class MainView(View):
    def get(self, request):
        companies = Company.objects.values('pk', 'name', 'logo').annotate(amount=Count('vacancies'))
        specialities = Specialty.objects.values('code', 'title').annotate(amount=Count('vacancies'))
        context = {
            'specialities': specialities,
            'companies': companies,
        }
        return render(request, 'index.html', context=context)


class ListVacanciesView(View):
    def get(self, request):
        context = {
            'vacancies': Vacancy.objects.all(),
        }
        return render(request, 'all-vacancies.html', context=context)


class VacanciesOfSpecialityView(View):
    def get(self, request, speciality):
        select_specialty = Specialty.objects.filter(code=speciality)
        if select_specialty.count() == 0:
            raise Http404
        else:
            context = {
                'vacancies': Vacancy.objects.filter(specialty__code=speciality),
                'select_specialty': select_specialty,
            }
            return render(request, 'vacancies.html', context=context)


class CompanyView(View):
    def get(self, request, id_company):
        company = Company.objects.filter(pk=id_company)
        if company.count() == 0:
            raise Http404
        else:
            vacancies_company = Vacancy.objects.filter(company__pk=id_company)
            context = {
                'company': company,
                'vacancies': vacancies_company,
            }
            return render(request, 'company.html', context=context)


class VacancyView(View):
    def get(self, request, id_vacancy):
        context = {
            'vacancy': Vacancy.objects.get(pk=id_vacancy),
        }
        return render(request, 'vacancy.html', context=context)
