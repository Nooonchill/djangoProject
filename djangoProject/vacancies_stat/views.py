from django.shortcuts import render
import pandas as pd
from django.shortcuts import render
from vacancies_stat.models import Person

def index_page(request):
    persons = Person.objects.all()
    s = ""
    for person in persons:
        s += f"<h3>{person}: возраст - {person.age}, должность - {person.job.lower()}</h3>"

    return render(request, 'index.html', context={"person_list": s})