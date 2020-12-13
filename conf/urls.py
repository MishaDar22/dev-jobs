"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from jobs.views import MainView, ListVacanciesView, VacanciesOfSpecialityView, CompanyView, VacancyView, \
    custom_handler404, ApplicateOnVacancy, MyCompany, MyVacancies, OneOfMyVacancy, MyCompanyLetsStart, MyCompanyCreate,\
    MyVacanciesLestsStart, MyVacanciesCreate
from login.views import register

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', ListVacanciesView.as_view(), name='vacancies-list'),
    path('vacancies/cat/<str:speciality>/', VacanciesOfSpecialityView.as_view(), name='vacancies-of-speciality'),
    path('companies/<int:id_company>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id_vacancy>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:id_vacancy>/send/', ApplicateOnVacancy.as_view()),
    path('mycompany/', MyCompany.as_view(), name='mycompany'),
    path('mycompany/letsstart', MyCompanyLetsStart.as_view(), name='letsstart'),
    path('mycompany/create/', MyCompanyCreate.as_view(), name='create'),
    path('mycompany/vacancies/', MyVacancies.as_view(), name='myvacancies'),
    path('mycompany/vacancies/<int:id_vacancy>/', OneOfMyVacancy.as_view(), name='myvacancy'),
    path('mycompany/vacancies/letsstart/', MyVacanciesLestsStart.as_view(), name='myfirstvacancy'),
    path('mycompany/vacancies/create/', MyVacanciesCreate.as_view(), name='createmyfirstvacancy'),
    path('admin/', admin.site.urls),
]

handler404 = custom_handler404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('', include("django.contrib.auth.urls")),
    path('register', register, name='register'),
]
