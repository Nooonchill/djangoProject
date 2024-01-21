from django.shortcuts import render
from build_graphics import build_year_bar_graph, build_salary_avg_graph, build_vacancies_percent_area_graph
from vacancies_stat.models import StatByYear, SalaryAvgAreaTop10, SalaryAvgAreaProfTop10, VacanciesPercentAreaTop10, VacanciesPercentAreaProfTop10


def index_page(request):
    return render(request, 'index.html', context={})


def demand_page(request):
    stats = StatByYear.objects.all()
    years = [int(stats[i].year) for i in range(len(stats))]
    salary_avg_year = build_year_bar_graph(years,
                                           [int(stats[i].salary_avg) for i in range(len(stats))],
                                      'Уровень зарплат по годам',
                                      'Cредняя з/п')
    salary_avg_year_prof = build_year_bar_graph(years,
                                                [int(stats[i].salary_avg_prof) for i in range(len(stats))],
                                           'Уровень зарплат по годам для профессии C#',
                                                'Cредняя з/п  C#')
    vacancies_amount = build_year_bar_graph(years,
                                            [int(stats[i].vacancies_amount) for i in range(len(stats))],
                                       'Количество вакансий по годам',
                                       'Количество вакансий')
    vacancies_amount_prof = build_year_bar_graph(years,
                                                 [int(stats[i].vacancies_amount_prof) for i in range(len(stats))],
                                            'Количество вакансий по годам для профессии C#',
                                            'Количество вакансий  C#')

    context = {'stats': stats,
               'salary_avg_year_graph': salary_avg_year,
               'salary_avg_year_prof_graph': salary_avg_year_prof,
               'vacancies_amount_graph': vacancies_amount,
               'vacancies_amount_prof_graph': vacancies_amount_prof}


    return render(request, 'demand.html', context)


def geography_page(request):
    salary_avg_area_stat = SalaryAvgAreaTop10.objects.all()
    salary_avg_area_graph = build_salary_avg_graph([salary_avg_area_stat[i].area_name for i in range(len(salary_avg_area_stat))],
                                                   [int(salary_avg_area_stat[i].salary_avg) for i in range(len(salary_avg_area_stat))],
                                                   'Средняя з/п' )
    salary_avg_area_prof_stat = SalaryAvgAreaProfTop10.objects.all()
    salary_avg_area_prof_graph = build_salary_avg_graph([salary_avg_area_prof_stat[i].area_name for i in range(len(salary_avg_area_prof_stat))],
                                                        [int(salary_avg_area_prof_stat[i].salary_avg_prof) for i in range(len(salary_avg_area_prof_stat))],
                                                        'Средняя з/п C#',
                                                        title=' C#')

    vacancies_percent_area_stat = VacanciesPercentAreaTop10.objects.all()
    vacancies_percent_area_graph = build_vacancies_percent_area_graph([vacancies_percent_area_stat[i].area_name for i in range(len(vacancies_percent_area_stat))],
                                                                      [vacancies_percent_area_stat[i].vacancies_percent for i in range(len(vacancies_percent_area_stat))])
    vacancies_percent_area_prof_stat = VacanciesPercentAreaProfTop10.objects.all()
    vacancies_percent_area_prof_graph = build_vacancies_percent_area_graph([vacancies_percent_area_stat[i].area_name for i in range(len(vacancies_percent_area_stat))],
                                                                           [vacancies_percent_area_prof_stat[i].vacancies_percent_prof for i in range(len(vacancies_percent_area_prof_stat))],
                                                                           'C#')

    context = {'salary_avg_area_stat': salary_avg_area_stat,
               'salary_avg_area_graph': salary_avg_area_graph,
               'salary_avg_area_prof_stat': salary_avg_area_prof_stat,
               'salary_avg_area_prof_graph': salary_avg_area_prof_graph,

               'vacancies_percent_area_stat': vacancies_percent_area_stat,
               'vacancies_percent_area_graph': vacancies_percent_area_graph,
               'vacancies_percent_area_prof_stat': vacancies_percent_area_prof_stat,
               'vacancies_percent_area_prof_graph': vacancies_percent_area_prof_graph}
    return render(request, 'geography.html', context)


def skills_page(request):
    return render(request, 'skills.html')

def last_vacs_page(request):
    return render(request, 'last_vacs.html')
