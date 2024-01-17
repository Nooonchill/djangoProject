import math
import pandas as pd
import sqlite3


conn = sqlite3.connect('db.sqlite3')
df_currency = pd.read_sql('SELECT * FROM vacancies_stat_currency', conn, index_col='date')
df_currency = df_currency.reset_index()
csv_merged = pd.read_sql('SELECT * FROM vacancies_stat_vacancy', conn, index_col='id')
df = csv_merged
df = df.assign(
    salary=((df['salary_to'].fillna(df['salary_from']) + df['salary_from'].fillna(df['salary_to'])) / 2),
    date=df['published_at'].apply(lambda x: x[:7])
)

df_currency = df_currency.fillna(-1)

for i in range(len(df)):
    if str(df.loc[i, 'salary_currency']) in ['None', 'RUR'] or df.loc[i, 'salary'] in ['None']:
        continue
    c = df_currency[df_currency['date'] == df.loc[i, 'date']][df.loc[i, 'salary_currency']].values[0]
    df.loc[i, 'salary'] = float(str(c))*df.loc[i, 'salary']

df['salary'] = df['salary'].apply(lambda x: None if x < 0.0 else x)
df['date'] = df['published_at'].apply(lambda x: x[:10])
df = df[['name', 'salary', 'area_name', 'date']]
df.to_sql('vacancies_stat_formedvacancy', conn, if_exists='append')