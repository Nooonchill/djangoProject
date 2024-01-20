from django.contrib import admin
from vacancies_stat.models import *

admin.site.register(Vacancy)
admin.site.register(Currency)
admin.site.register(FormedVacancy)
admin.site.register(StatByYear)
admin.site.register(StatByArea)
admin.site.register(SalaryAvgAreaTop10)
admin.site.register(SalaryAvgAreaProfTop10)
admin.site.register(VacanciesPercentAreaTop10)
admin.site.register(VacanciesPercentAreaProfTop10)
