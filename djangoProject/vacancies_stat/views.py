from django.shortcuts import render
from draw_graphics import draw_salary_avg_year, draw_vacancy_amount_year
from vacancies_stat.models import StatByYear

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

