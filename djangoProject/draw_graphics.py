from io import StringIO

from matplotlib import pyplot as plt

def draw_salary_avg_year(stats, is_prof=False):
    years = [float(stats[i].year) for i in range(len(stats))]
    if is_prof:
        values = [float(stats[i].salary_avg_prof) for i in range(len(stats))]
    else:
        values = [float(stats[i].salary_avg) for i in range(len(stats))]
    plt.rcParams.update({'font.size': 8})
    plt.bar(years, values, label='средняя з/п' + (int(is_prof)*' C#') )

    plt.title('Уровень зарплат по годам' + (int(is_prof)*'для профессии C#'))
    plt.legend()
    plt.grid(axis='y')
    plt.xticks([float(stats[i].year) for i in range(len(stats))], rotation=90)
    imgdata = StringIO()
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data