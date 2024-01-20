from io import StringIO

from django.shortcuts import render
import pandas as pd
from django.shortcuts import render
from matplotlib import pyplot as plt

from vacancies_stat.models import StatByYear

def index_page(request):
    stats = StatByYear.objects.all()
    df = pd.DataFrame(stats)

    years = list(range(2003, 2024))
    plt.rcParams.update({'font.size': 8})
    plt.bar(years, [float(stats[i].salary_avg) for i in range(len(stats))], label='средняя з/п', width=0.8)

    plt.title('Уровень зарплат по годам')
    plt.legend()
    plt.grid(axis='y')
    plt.xticks(years, rotation=90)
    imgdata = StringIO()
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()



    context = {'stats': stats, 'graph': data}


    return render(request, 'index.html', context)

