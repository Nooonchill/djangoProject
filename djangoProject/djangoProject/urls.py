from django.contrib import admin
from django.urls import path

from vacancies_stat.views import index_page, demand_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('demand/', demand_page),
]
