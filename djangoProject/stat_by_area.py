import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

def format_vacancy_percent(vacancies):
    vacancy_percent = round(vacancies['area_name'].value_counts(normalize=True), 4)
    vacancy_percent = (vacancy_percent
                       .to_frame()
                       .sort_values(['proportion', 'area_name'], ascending=[False, True]))
    return vacancy_percent['proportion'].to_dict()


def count_salary_cities(vacancies):
    salary_city = (vacancies[['area_name', 'salary']]
                   .groupby('area_name')
                   .mean())
    salary_city['salary'] = salary_city['salary'].apply(lambda x: round(x) if str(x)!='nan' else None)
    return salary_city['salary'].to_dict()


conn = sqlite3.connect('db.sqlite3')
vacancies = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy', conn, index_col='id')
vacancies_prof = vacancies[vacancies['name'].str.contains('c#|c sharp|шарп|с#', case=False)]

stat_by_area = {'salary_avg': count_salary_cities(vacancies),
               'vacancies_percent': format_vacancy_percent(vacancies),
               'salary_avg_prof': count_salary_cities(vacancies_prof),
               'vacancies_percent_prof': format_vacancy_percent(vacancies_prof)}
stat_by_area = pd.DataFrame(stat_by_area)
stat_by_area.index.rename('area_name', inplace=True)
stat_by_area.to_sql('vacancies_stat_statbyarea', conn, if_exists='append')

