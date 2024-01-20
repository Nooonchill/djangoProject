from django.shortcuts import render
import pandas as pd
from django.shortcuts import render
from vacancies_stat.models import Person

def index_page(request):
    pass
    #return render(request, 'index.html', context={"graph": create_plot()})