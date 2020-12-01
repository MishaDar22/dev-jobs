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
from django.urls import path

from jobs.views import MainView, ListVacanciesView, VacanciesOfSpecialityView, CompanyView, VacancyView, \
    custom_handler404

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', ListVacanciesView.as_view(), name='vacancies-list'),
    path('vacancies/cat/<str:speciality>/', VacanciesOfSpecialityView.as_view(), name='vacancies-of-speciality'),
    path('companies/<int:id_company>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:id_vacancy>/', VacancyView.as_view(), name='vacancy'),
]

handler404 = custom_handler404
