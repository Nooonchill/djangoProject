from django.contrib import admin
from django.urls import path

from vacancies_stat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index_page'),
    path('demand/', demand_page, name='demand_page'),
    path('geography/', geography_page, name='geography_page'),
    path('skills/', skills_page, name='skills_page'),
    path('last_vacs/', last_vacs_page, name='last_vacs_page')
]
