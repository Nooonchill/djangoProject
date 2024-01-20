from io import StringIO

from matplotlib import pyplot as plt

def draw_salary_avg_year(stats, is_prof=False):
    years = [int(stats[i].year) for i in range(len(stats))]
    if is_prof:
        values = [int(stats[i].salary_avg_prof) for i in range(len(stats))]
    else:
        values = [int(stats[i].salary_avg) for i in range(len(stats))]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.bar(years, values, label='средняя з/п' + (int(is_prof)*' C#') )

    ax.set_title('Уровень зарплат по годам' + (int(is_prof)*' для профессии C#'))
    ax.legend()
    ax.grid(axis='y')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=90)
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def draw_vacancy_amount_year(stats, is_prof=False):
    years = [int(stats[i].year) for i in range(len(stats))]
    if is_prof:
        values = [int(stats[i].vacancies_amount_prof) for i in range(len(stats))]
    else:
        values = [int(stats[i].vacancies_amount) for i in range(len(stats))]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.bar(years, values, label='Количество вакансий' + (int(is_prof)*' C#') )

    ax.set_title('Количество вакансий по годам' + (int(is_prof)*' для профессии C#'))
    ax.legend()
    ax.grid(axis='y')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=90)
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def draw_salary_avg_area(stats, is_prof=False):
    area = [stats[i].area_name for i in range(len(stats))]
    area = [s.replace('-', '-\n').replace(' ', '\n') for s in area]
    if is_prof:
        values = [int(stats[i].salary_avg_prof) for i in range(len(stats))]
    else:
        values = [int(stats[i].salary_avg) for i in range(len(stats))]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.barh(area, values, label='Средняя зп' + (int(is_prof)*' C#') )
    ax.invert_yaxis()
    ax.set_title('Уровень зарплат по городам')
    ax.grid(axis='x')
    ax.set_yticks(area)
    ax.set_yticklabels(area, fontsize=6, verticalalignment='center', horizontalalignment='right')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def draw_vacancies_percent_area(stats, is_prof=False):
    area = [stats[i].area_name for i in range(len(stats))]
    area = [s.replace('-', '-\n').replace(' ', '\n') for s in area]
    if is_prof:
        values = [stats[i].vacancies_percent_prof for i in range(len(stats))]
    else:
        values = [stats[i].vacancies_percent for i in range(len(stats))]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.pie(values, labels=area, textprops={'fontsize': 6})
    ax.set_title('Доля ваканский по городам')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

