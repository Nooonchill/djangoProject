import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

def format_pd(df, vac=""):
    vacancies = (df
                 .assign(year=(df['date'].str[:4]))
                 )
    vacancies['year'] = vacancies['year'].apply(lambda x: int(x))
    vacancies_prof = vacancies[vacancies['name'].str.contains(vac, case=False)]
    return vacancies, vacancies_prof


def count_salary_avg(vacancies, key='year'):
    vacancies_salary_avg = (
        vacancies[[key, 'salary']]
            .groupby(key)
            .mean()
    )
    vacancies_salary_avg = vacancies_salary_avg.loc[vacancies_salary_avg['salary'] <= 10000000]
    vacancies_salary_avg = vacancies_salary_avg['salary'].apply(lambda x: round(x) if str(x)!='None' else None).to_dict()
    return vacancies_salary_avg


def count_vacancies_amount(vacancies, key='year'):
    vacancies_amount = vacancies[key].value_counts().sort_index().to_dict()
    return vacancies_amount


def find_vacancy_percent(vacancies):
    vacancy_percent = round(vacancies['area_name'].value_counts(normalize=True), 4)
    return vacancy_percent


def format_vacancy_percent(vacancies):
    vacancy_percent = find_vacancy_percent(vacancies)
    vacancy_percent = (vacancy_percent
                       .to_frame()
                       .sort_values(['proportion', 'area_name'], ascending=[False, True])
                       .head(10))
    return vacancy_percent['proportion'].to_dict()


def count_salary_cities(vacancies):
    vacancy_percent = find_vacancy_percent(vacancies)
    vacancies_prof = vacancies[vacancies['area_name'].isin(vacancy_percent[vacancy_percent > 0.01].index)]
    salary_city = (vacancies_prof[['area_name', 'salary']]
                   .groupby('area_name')
                   .mean())
    salary_city['salary'] = (salary_city['salary']
                             .apply(lambda x: round(x)))
    salary_city = (salary_city
                   .sort_values(['salary', 'area_name'], ascending=[False, True])
                   .head(10))
    return salary_city['salary'].to_dict()


def format_year_stat(salary_avg_year, amount_vacancies_year):
    years_stat = [['Год', 'Средняя зарплата', 'Количество вакансий']]
    for year in salary_avg_year.keys():
        row = [year, salary_avg_year[year], amount_vacancies_year[year]]
        years_stat.append(row)
    return years_stat


def format_cities_stat(salary_cities, vacancy_percent):
    salary_stat = [['Город', 'Доля вакансий, %']]
    for city1 in salary_cities.keys():
        row = [city1, salary_cities[city1]*100]
        salary_stat.append(row)
    percent_stat = [['Город', 'Уровень зарплат']]
    for city2 in vacancy_percent.keys():
        row = [city2, vacancy_percent[city2]]
        percent_stat.append(row)
    return [salary_stat, percent_stat]


def correct_dic(dic):
    corrected_dic = {}
    for year in range(2003, 2024):
        if year not in dic.keys():
            corrected_dic[year] = 0
        else:
            corrected_dic[year] = dic[year]
    return corrected_dic

def create_plot():
    vac = 'c#'
    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy', conn, index_col='id')
    vacancies, vacancies_prof = format_pd(df, vac)
    print(vacancies, vacancies_prof)
    fig, sub = plt.subplots(2, 2)
    width = 0.4
    years= list(range(2003, 2024))
    plt.rcParams.update({'font.size': 8})
    sub[0,0].bar([i-width/2 for i in years], count_salary_avg(vacancies).values(), label='средняя з/п', width=width)
    sub[0,0].bar([i+width/2 for i in years], correct_dic(count_salary_avg(vacancies_prof)).values(), label='з/п программист', width=width)
    sub[0,0].set_title('Уровень зарплат по годам')
    sub[0,0].legend()
    sub[0,0].grid(axis='y')
    sub[0,0].set_xticks(years)
    sub[0,0].set_xticklabels(years, rotation=90)

    sub[0,1].bar([i-width/2 for i in years], count_vacancies_amount(vacancies).values(), label='количество вакансий', width=width)
    sub[0,1].bar([i for i in years], correct_dic(count_vacancies_amount(vacancies_prof)).values(), label='количество вакансий программист', width=width)
    sub[0,1].set_title('Количество вакансий по годам')
    sub[0,1].legend()
    sub[0,1].grid(axis='y')
    sub[0,1].set_xticks(years)
    sub[0,1].set_xticklabels(years, rotation=90)

    salary_cities = count_salary_cities(vacancies)
    cities = list(salary_cities.keys())
    cities = [s.replace('-', '-\n').replace(' ', '\n') for s in cities]
    cities_salary = list(salary_cities.values())
    sub[1,0].barh(cities, cities_salary)
    sub[1,0].invert_yaxis()
    sub[1,0].set_title('Уровень зарплат по городам')
    sub[1,0].grid(axis='x')
    sub[1,0].set_yticks(cities)
    sub[1,0].set_yticklabels(cities, fontsize=6, verticalalignment='center', horizontalalignment='right')


    vacancy_percent = find_vacancy_percent(vacancies)
    low_vacancies = vacancies[vacancies['area_name'].isin(vacancy_percent[vacancy_percent < 0.01].index)]
    data = format_vacancy_percent(vacancies)
    data['Другие'] = len(low_vacancies)/len(vacancies)


    sorted_dict = {}
    sorted_keys = sorted(data, key=data.get)

    for w in sorted_keys:
        sorted_dict[w] = data[w]

    sub[1,1].pie(list(sorted_dict.values()), labels=list(sorted_dict.keys()), textprops={'fontsize': 6})
    sub[1,1].set_title('Доля ваканский по городам')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

conn = sqlite3.connect('db.sqlite3')
df = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy', conn, index_col='id')
vacancies, vacancies_prof = format_pd(df, 'c#')
print(pd.DataFrame({'salary_avg': count_salary_avg(vacancies),
                    'vacancies_amount': count_vacancies_amount(vacancies),
                    'salary_avg_prof': count_salary_avg(vacancies_prof),
                    'vacancies_amount_prof': count_vacancies_amount(vacancies_prof)}))
print(pd.DataFrame({'salary_avg': count_salary_avg(vacancies, key='area_name'),
                    'vacancies_amount': count_vacancies_amount(vacancies, key='area_name'),
                    'salary_avg_prof': count_salary_avg(vacancies_prof, key='area_name'),
                    'vacancies_amount_prof': count_vacancies_amount(vacancies_prof, key='area_name')}))