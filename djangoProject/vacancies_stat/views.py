from django.shortcuts import render
from draw_graphics import draw_salary_avg_year, draw_vacancy_amount_year, draw_salary_avg_area, draw_vacancies_percent_area
from vacancies_stat.models import StatByYear, SalaryAvgAreaTop10, SalaryAvgAreaProfTop10, VacanciesPercentAreaTop10, VacanciesPercentAreaProfTop10


def index_page(request):
    return render(request, 'index.html', context={})

def demand_page(request):
    stats = StatByYear.objects.all()
    salary_avg_year = draw_salary_avg_year(stats)
    salary_avg_year_prof = draw_salary_avg_year(stats, is_prof=True)
    vacancies_amount = draw_vacancy_amount_year(stats)
    vacancies_amount_prof = draw_vacancy_amount_year(stats, is_prof=True)

    context = {'stats': stats,
               'salary_avg_year_graph': salary_avg_year,
               'salary_avg_year_prof_graph': salary_avg_year_prof,
               'vacancies_amount_graph': vacancies_amount,
               'vacancies_amount_prof_graph': vacancies_amount_prof}


    return render(request, 'demand.html', context)

def geography_page(request):
    salary_avg_area_stat = SalaryAvgAreaTop10.objects.all()
    salary_avg_area_graph = draw_salary_avg_area(salary_avg_area_stat)
    salary_avg_area_prof_stat = SalaryAvgAreaProfTop10.objects.all()
    salary_avg_area_prof_graph = draw_salary_avg_area(salary_avg_area_prof_stat, is_prof=True)

    vacancies_percent_area_stat = VacanciesPercentAreaTop10.objects.all()
    vacancies_percent_area_graph = draw_vacancies_percent_area(vacancies_percent_area_stat)
    vacancies_percent_area_prof_stat = VacanciesPercentAreaProfTop10.objects.all()
    vacancies_percent_area_prof_graph = draw_vacancies_percent_area(vacancies_percent_area_prof_stat, is_prof=True)

    context = {'salary_avg_area_stat': salary_avg_area_stat,
               'salary_avg_area_graph': salary_avg_area_graph,
               'salary_avg_area_prof_stat': salary_avg_area_prof_stat,
               'salary_avg_area_prof_graph': salary_avg_area_prof_graph,

               'vacancies_percent_area_stat': vacancies_percent_area_stat,
               'vacancies_percent_area_graph': vacancies_percent_area_graph,
               'vacancies_percent_area_prof_stat': vacancies_percent_area_prof_stat,
               'vacancies_percent_area_prof_graph': vacancies_percent_area_prof_graph}
    return render(request, 'geography.html', context)
