import sqlite3
import pandas as pd


def count_salary_avg(vacancies, key='year'):
    vacancies_salary_avg = (
        vacancies[[key, 'salary']]
            .groupby(key)
            .mean()
    )
    vacancies_salary_avg = vacancies_salary_avg.loc[vacancies_salary_avg['salary'] <= 10000000]
    vacancies_salary_avg = vacancies_salary_avg['salary'].apply(lambda x: round(x) if str(x)!='None' else None).to_dict()
    return vacancies_salary_avg


conn = sqlite3.connect('db.sqlite3')
df = pd.read_sql('SELECT * FROM vacancies_stat_formedvacancy LIMIT 100000', conn, index_col='id')
vacancies = (df
             .assign(year=(df['date'].str[:4]))
             )
vacancies['year'] = vacancies['year'].apply(lambda x: int(x))
vacancies_prof = vacancies[vacancies['name'].str.contains('c#|c sharp|шарп|с#', case=False)]

stat_by_year = {'salary_avg': count_salary_avg(vacancies),
                'vacancies_amount': vacancies['year'].value_counts().sort_index().to_dict(),
                'salary_avg_prof': count_salary_avg(vacancies_prof),
                'vacancies_amount_prof': vacancies_prof['year'].value_counts().sort_index().to_dict()}
print(stat_by_year)
stat_by_year = pd.DataFrame(stat_by_year)
print(stat_by_year)

