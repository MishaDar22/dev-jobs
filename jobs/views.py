from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404
from django.urls import reverse
from django.views import View

from jobs.forms import ApplicationForm, CompanyForm, VacancyForm
from jobs.models import Specialty, Company, Vacancy, Application


def custom_handler404(request, exception):
    return HttpResponseNotFound('Что-то сломалось :(')


class MainView(View):
    def get(self, request):
        companies = Company.objects.values('pk', 'name', 'logo').annotate(amount=Count('vacancies'))
        specialities = Specialty.objects.values('code', 'title', 'picture').annotate(amount=Count('vacancies'))
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
            'form': ApplicationForm,
        }
        return render(request, 'vacancy.html', context=context)


class ApplicateOnVacancy(View):
    def post(self, request, id_vacancy):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user if request.user else '1'
            vacancy = Vacancy.objects.get(pk=id_vacancy)
            application = Application.objects.create(
                written_username=data['written_username'],
                written_phone=data['written_phone'],
                written_cover_letter=data['written_cover_letter'],
                user=user,
                vacancy=vacancy,
            )
            return render(request, 'sent.html', vacancy)
        return render(request, 'vacancy.html', {'form': form})


class MyCompany(View):
    def get(self, request):
        company = request.user.mycompany.all()
        no_company = 0
        user = request.user
        if len(company) == no_company:
            return redirect(reverse('letsstart'))
        else:
            form = CompanyForm(
                initial={
                    'name': request.user.mycompany.first().name,
                    'location': request.user.mycompany.first().location,
                    'logo': request.user.mycompany.first().logo,
                    'description': request.user.mycompany.first().description,
                    'employee_count': request.user.mycompany.first().employee_count,
                    'owner': user,
                }
            )
            context = {
                'form': form,
            }
        return render(request, 'company-edit.html', context=context)

    def post(self, request):
        form = CompanyForm(request.POST)
        company = request.user.mycompany.first()
        if form.is_valid():
            data = form.cleaned_data
            company.name = data['name']
            company.location = data['location']
            company.logo = data['logo']
            company.description = data['description']
            company.employee_count = data['employee_count']
            company.save()

            return redirect('/mycompany/')
        return render(request, 'company_new_create.html', {'form': form})


class MyCompanyLetsStart(View):
    def get(self, request):
        return render(request, 'company-lets-start.html')


class MyCompanyCreate(View):
    def get(self, request):
        context = {
            'form': CompanyForm,
        }
        return render(request, 'company_new_create.html', context=context)

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            company = Company.objects.create(
                name=data['name'],
                location=data['location'],
                logo=data['logo'],
                description=data['description'],
                employee_count=data['employee_count'],
                owner=user,
            )
            return redirect('/mycompany/')
        return render(request, 'company_new_create.html', {'form': form})


class MyVacancies(View):
    def get(self, request):
        company = request.user.mycompany.first()
        vacancies = company.vacancies.all()
        zero_vacancies = 0
        if len(vacancies) == zero_vacancies:
            return redirect('/mycompany/vacancies/letsstart/')

        context = {
            'vacancies': vacancies,
        }
        return render(request, 'vacancy-list.html', context=context)


class MyVacanciesLestsStart(View):
    def get(self, request):
        return render(request, 'vacancy_lets-start.html')


class MyVacanciesCreate(View):
    def get(self, request):
        form = VacancyForm()
        context = {
            'form': form,
        }
        return render(request, 'vacancy-create.html', context=context)

    def post(self, request):
        form = VacancyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            company = request.user.mycompany.first()
            vacancy = Vacancy.objects.create(
                title=data['title'],
                description=data['description'],
                skills=data['skills'],
                salary_min=data['salary_min'],
                salary_max=data['salary_max'],
                specialty=data['specialty'],
                company=company,
            )
            return redirect('/mycompany/vacancies/')
        return render(request, 'company_new_create.html', {'form': form})


class OneOfMyVacancy(View):
    def get(self, request, id_vacancy):
        company = request.user.mycompany.first()
        vacancy = company.vacancies.get(id=id_vacancy)
        applications = vacancy.applications.all()
        form = VacancyForm(initial={
            'title': vacancy.title,
            'description': vacancy.description,
            'skills': vacancy.skills,
            "salary_min": vacancy.salary_min,
            'salary_max': vacancy.salary_max,
            'specialty': Specialty.objects.all(),
        })
        context = {
            'form': form,
            'applications': applications,
        }
        return render(request, 'vacancy-edit.html', context=context)

    def post(self, request, id_vacancy):
        form = VacancyForm(request.POST)
        if form.is_valid():
            company = request.user.mycompany.first()
            vacancy = company.vacancies.get(id=id_vacancy)
            data = form.cleaned_data
            vacancy.title = data['title']
            vacancy.specialty_id = data['specialty']
            vacancy.salary_min = data['salary_min']
            vacancy.salary_max = data['salary_max']
            vacancy.description = data['description']
            vacancy.skills = data['skills']
            vacancy.save()
            return redirect(request.path)
        return render(request, 'company_new_create.html', {'form': form})
