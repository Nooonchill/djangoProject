from io import StringIO

from matplotlib import pyplot as plt


def save_fig(fig):
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data

def build_year_bar_graph(years, values, title, label):
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.bar(years, values, label= label )
    ax.set_title(title)
    ax.legend()
    ax.grid(axis='y')
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=90)
    return save_fig(fig)

def build_salary_avg_graph(area, values, label, title=''):
    area = [s.replace('-', '-\n').replace(' ', '\n') for s in area]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.barh(area, values, label=label)
    ax.invert_yaxis()
    ax.set_title(f'Уровень зарплат по городам {title}' )
    ax.grid(axis='x')
    ax.set_yticks(area)
    ax.set_yticklabels(area, fontsize=6, verticalalignment='center', horizontalalignment='right')
    return save_fig(fig)

def build_vacancies_percent_area_graph(area, values, title=''):
    area = [s.replace('-', '-\n').replace(' ', '\n') for s in area]
    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots()
    ax.pie(values, labels=area, textprops={'fontsize': 6})
    ax.set_title(f'Доля ваканский по городам {title}')

    return save_fig(fig)
