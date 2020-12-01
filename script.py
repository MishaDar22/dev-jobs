import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

import jobs.data
from jobs.models import Specialty, Company, Vacancy

if __name__ == '__main__':
    for one_specialty in jobs.data.specialties:
        specialty = Specialty.objects.create(
            code=one_specialty['code'],
            title=one_specialty['title'],
            picture='https://place-hold.it/100x60',
        )
    for one_company in jobs.data.companies:
        company = Company.objects.create(
            name=one_company['title'],
            location=one_company['location'],
            logo='https://place-hold.it/100x60',
            description=one_company['description'],
            employee_count=one_company['employee_count'],
        )
    for job in jobs.data.jobs:
        vacancy = Vacancy.objects.create(
            title=job['title'],
            specialty_id=Specialty.objects.get(code=job['speciality']).pk,
            company_id=job['company'],  # оставлю здесь такой вариант. Так как в бд не передаем id, который
            # есть в data.py в companies = [{'id':1...}...].
            skills=job['skills'],
            description=job['description'],
            salary_min=job['salary_from'],
            salary_max=job['salary_to'],
            published_at=job['posted'],
        )
