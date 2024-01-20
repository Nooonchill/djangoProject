import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')
stat_by_area = pd.read_sql('SELECT * FROM vacancies_stat_statbyarea', conn, index_col='area_name')

salary_avg_area_for_graph = (stat_by_area[stat_by_area['vacancies_percent'] > 0.01]
                             .sort_values('salary_avg', ascending=False)
                             [['salary_avg']]
                             .head(10))

salary_avg_area_for_graph.to_sql('vacancies_stat_salaryavgareatop10', conn, if_exists='append')

salary_avg_area_prof_for_graph = (stat_by_area[stat_by_area['vacancies_percent'] > 0.01]
                             .sort_values('salary_avg_prof', ascending=False)
                             [['salary_avg_prof']]
                             .head(10))
salary_avg_area_prof_for_graph.to_sql('vacancies_stat_salaryavgareaproftop10', conn, if_exists='append')

vacancies_percent_area_for_graph = (stat_by_area[stat_by_area['vacancies_percent'] > 0.01]
                                    .sort_values('vacancies_percent', ascending=False)
                                    [['vacancies_percent']]
                                    .head(10))
vacancies_percent_area_for_graph.loc['Другие'] = 1- sum(vacancies_percent_area_for_graph['vacancies_percent'].values)
vacancies_percent_area_for_graph.to_sql('vacancies_stat_vacanciespercentareatop10', conn, if_exists='append')


vacancies_percent_area_prof_for_graph = (stat_by_area[stat_by_area['vacancies_percent'] > 0.01]
                                         .sort_values('vacancies_percent_prof', ascending=False)
                                         [['vacancies_percent_prof']]
                                         .head(10))
vacancies_percent_area_prof_for_graph.loc['Другие'] = 1- sum(vacancies_percent_area_prof_for_graph['vacancies_percent_prof'].values)
vacancies_percent_area_prof_for_graph.to_sql('vacancies_stat_vacanciespercentareaproftop10', conn, if_exists='append')

print(salary_avg_area_for_graph)
print(salary_avg_area_prof_for_graph)
print(vacancies_percent_area_for_graph)
print(vacancies_percent_area_prof_for_graph)
