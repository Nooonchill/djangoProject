from django.contrib import admin
from vacancies_stat.models import *

admin.site.register(Person)
admin.site.register(Vacancy)
admin.site.register(Currency)
admin.site.register(FormedVacancy)
admin.site.register(StatByYear)
admin.site.register(StatByArea)