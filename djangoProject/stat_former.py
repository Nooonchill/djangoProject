import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

def format_pd(df, vac=""):
    vacancies = (df
                 .assign(year=(df['date'].str[:4]))
                 )
    vacancies['year'] = vacancies['year'].apply(lambda x: int(x))
    vacancies_prof = vacancies[vacancies['name'].str.contains('c#|c sharp|шарп|с#', case=False)]
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
                       .sort_values(['proportion', 'area_name'], ascending=[False, True]))
    return vacancy_percent['proportion'].to_dict()


def count_salary_cities(vacancies):
    salary_city = (vacancies[['area_name', 'salary']]
                   .groupby('area_name')
                   .mean())
    salary_city['salary'] = (salary_city['salary']
                             .apply(lambda x: round(x) if str(x)!='nan' else None))
    return salary_city['salary'].to_dict()

"""
def create_plot():
    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy', conn, index_col='id')
    vacancies, vacancies_prof = format_pd(df, 'c#')
    years_stat = pd.DataFrame({'salary_avg': count_salary_avg(vacancies),
                               'vacancies_amount': count_vacancies_amount(vacancies),
                               'salary_avg_prof': correct_dic(count_salary_avg(vacancies_prof)),
                               'vacancies_amount_prof': correct_dic(count_vacancies_amount(vacancies_prof))})

    cities_stat = pd.DataFrame({'salary_avg': count_salary_cities(vacancies),
                                'vacancies_amount': format_vacancy_percent(vacancies),
                                'salary_avg_prof': count_salary_cities(vacancies_prof),
                                'vacancies_amount_prof': format_vacancy_percent(vacancies_prof)})
    fig, sub = plt.subplots(2, 2)
    width = 0.4
    years= list(range(2003, 2024))
    plt.rcParams.update({'font.size': 8})
    sub[0,0].bar([i-width/2 for i in years], years_stat['salary_avg'].to_dict().values(), label='средняя з/п', width=width)
    sub[0,0].bar([i+width/2 for i in years], years_stat['salary_avg_prof'].to_dict().values(), label='з/п c#', width=width)
    sub[0,0].set_title('Уровень зарплат по годам')
    sub[0,0].legend()
    sub[0,0].grid(axis='y')
    sub[0,0].set_xticks(years)
    sub[0,0].set_xticklabels(years, rotation=90)

    sub[0,1].bar([i-width/2 for i in years], years_stat['vacancies_amount'].to_dict().values(), label='количество вакансий', width=width)
    sub[0,1].bar([i for i in years], years_stat['vacancies_amount_prof'].to_dict().values(), label='количество вакансий c#', width=width)
    sub[0,1].set_title('Количество вакансий по годам')
    sub[0,1].legend()
    sub[0,1].grid(axis='y')
    sub[0,1].set_xticks(years)
    sub[0,1].set_xticklabels(years, rotation=90)


    data = cities_stat['salary_avg'].to_dict()
    print(data)
    data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:10])
    print(data)
    cities = list(data.keys())
    cities = [s.replace('-', '-\n').replace(' ', '\n') for s in cities]
    cities_salary = list(data.values())

    sub[1,0].barh(cities, cities_salary)
    sub[1,0].invert_yaxis()
    sub[1,0].set_title('Уровень зарплат по городам')
    sub[1,0].grid(axis='x')
    sub[1,0].set_yticks(cities)
    sub[1,0].set_yticklabels(cities, fontsize=6, verticalalignment='center', horizontalalignment='right')

    data = cities_stat['vacancies_amount'].to_dict()
    data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:10])

    sub[1,1].pie(list(data.values()), labels=list(data.keys()), textprops={'fontsize': 6})
    sub[1,1].set_title('Доля ваканский по городам')
    plt.show()
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data
"""

conn = sqlite3.connect('db.sqlite3')
df = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy LIMIT 1000', conn, index_col='id')
vacancies, vacancies_prof = format_pd(df, 'c#')
stat_by_year = {'salary_avg': count_salary_avg(vacancies),
              'vacancies_amount': count_vacancies_amount(vacancies),
              'salary_avg_prof': count_salary_avg(vacancies_prof),
              'vacancies_amount_prof': count_vacancies_amount(vacancies_prof)}
print(stat_by_year)
stat_by_year = pd.DataFrame(stat_by_year)
cities_stat = {'salary_avg': count_salary_cities(vacancies),
               'vacancies_amount': format_vacancy_percent(vacancies),
               'salary_avg_prof': count_salary_cities(vacancies_prof),
               'vacancies_amount_prof': format_vacancy_percent(vacancies_prof)}
print(cities_stat)
cities_stat = pd.DataFrame(cities_stat)
cities_stat = cities_stat.sort_values('salary_avg', ascending=False)
print(cities_stat[['salary_avg', 'vacancies_amount']])
