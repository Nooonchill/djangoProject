import sqlite3
import pandas as pd
from collections import Counter

conn = sqlite3.connect('db.sqlite3')
df = pd.read_sql('SELECT name, key_skills, date FROM vacancies_stat_vacancy LIMIT 1236484', conn)
df = df.assign(year=df['date'].str[:4])
df = df.dropna()

df['key_skills'] = df['key_skills'].apply(lambda x: x.split('\n'))
df = df[['key_skills', 'year']]
df = df.groupby(by='year').sum()
dic = df['key_skills'].to_dict()
print(df['key_skills'].to_dict())
for i in dic.keys():
    print(Counter(dic[i]))


