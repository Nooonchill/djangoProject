from django.shortcuts import render
import pandas as pd
from django.shortcuts import render
from vacancies_stat.models import Person
from stat_create import create_plot

def index_page(request):

    return render(request, 'index.html', context={"graph": create_plot()})