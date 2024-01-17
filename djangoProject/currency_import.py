import pandas as pd
import datetime
import sqlite3

valutes = ['BYR','USD','EUR','KZT','UAH','AZN','KGS','UZS','GEL']
data = {'date': [], 'BYR': [], 'USD': [], 'EUR': [], 'KZT': [], 'UAH': [], 'AZN': [], 'KGS': [], 'UZS': [], 'GEL': []}

start_date = datetime.date(2003, 1, 1)
end_date = datetime.date(2024, 1, 1)
while start_date <= end_date:
	month = start_date.strftime('%m')
	year = start_date.strftime('%Y')
	url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month}/{year}"
	df = pd.read_xml(url, encoding='windows-1251')
	data['date'].append(start_date.strftime('%Y-%m'))
	for valute in valutes:
		rate = df[df['CharCode']==valute]['VunitRate'].values
		if len(rate)>0:
			data[valute].append(round(float(rate[0].replace(',','.')), 9))
		else:
			data[valute].append(None)
	start_date = start_date.replace(day=1) + datetime.timedelta(days=32)
	start_date = start_date.replace(day=1)
df = pd.DataFrame(data)
df = df.set_index('date')
conn = sqlite3.connect('db.sqlite3')
df.to_sql('vacancies_stat_currency', conn, if_exists='append')
