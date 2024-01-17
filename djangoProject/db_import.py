import pandas as pd
import sqlite3

df = pd.read_csv('vacancies.csv')
conn = sqlite3.connect('db.sqlite3')
df.index.rename('id', inplace= True )
df = df.assign(
	salary=((df['salary_to'].fillna(df['salary_from']) + df['salary_from'].fillna(df['salary_to'])) / 2),
	date=df['published_at'].apply(lambda x: x[:7]))

df.to_sql('vacancies_stat_vacancy', conn, if_exists='append')
