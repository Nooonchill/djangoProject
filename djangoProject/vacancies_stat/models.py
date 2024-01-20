from django.db import models


class Vacancy(models.Model):
    name = models.CharField("Название", max_length=256)
    key_skills = models.CharField("Навыки", max_length=256)
    salary_from = models.DecimalField("Зарплата от", max_digits=16, decimal_places=1)
    salary_to = models.DecimalField("Зарплата до", max_digits=16, decimal_places=1)
    salary_currency = models.CharField("Валюта", max_length=4)
    area_name = models.CharField("Город", max_length=128)
    published_at = models.DateTimeField("Дата и время публикации")
    salary = models.DecimalField("Зарплата", max_digits=16, decimal_places=1, null=True)
    date = models.DateTimeField("Дата публикации", null=True)

    def __str__(self):
        return f"Вакансия {self.name}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Currency(models.Model):
    date = models.CharField("Дата", primary_key = True, max_length=7)
    USD = models.CharField("USD", max_length=3, null=True)
    BYR = models.CharField("BYR", max_length=3, null=True)
    EUR = models.CharField("EUR", max_length=3, null=True)
    KZT = models.CharField("KZT", max_length=3, null=True)
    UAH = models.CharField("UAH", max_length=3, null=True)
    AZN = models.CharField("AZN", max_length=3, null=True)
    KGS = models.CharField("KGS", max_length=3, null=True)
    UZS = models.CharField("UZS", max_length=3, null=True)
    GEL = models.CharField("GEL", max_length=3, null=True)

    def __str__(self):
        return f"Курс валют за {self.date}"

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

class FormedVacancy(models.Model):
    name = models.CharField("Название", max_length=256)
    area_name = models.CharField("Город", max_length=128)
    salary = models.DecimalField("Зарплата", max_digits=16, decimal_places=1, null=True)
    date = models.CharField("Дата публикации", max_length=10, null=True)

    def __str__(self):
        return f"Вакансия {self.name}"

    class Meta:
        verbose_name = "Форматированная вакансия"
        verbose_name_plural = "Форматированные вакансии"

class StatByYear(models.Model):
    year = models.IntegerField('Год', primary_key=True, default=0)
    salary_avg = models.DecimalField('Средняя з/п', max_digits=16, decimal_places=1)
    vacancies_amount = models.IntegerField('Количество вакансий')
    salary_avg_prof = models.DecimalField('Средняя з/п C#', max_digits=16, decimal_places=1)
    vacancies_amount_prof = models.IntegerField('Количество вакансий C#')

    def __str__(self):
        return f"Статистика по {self.year} году"

    class Meta:
        verbose_name = "Годовая статистика"
        verbose_name_plural = "Статистика по годам"

class StatByArea(models.Model):
    area_name = models.CharField("Город", max_length=128, primary_key=True)
    salary_avg = models.DecimalField("Средняя з/п ", max_digits=16, decimal_places=1, null=True)
    vacancies_percent = models.DecimalField('Доля вакансий', max_digits=4, decimal_places=3)
    salary_avg_prof = models.DecimalField("Средняя з/п С#", max_digits=16, decimal_places=1, null=True)
    vacancies_percent_prof = models.DecimalField("Доля вакансий С#", max_digits=16, decimal_places=1, null=True)

    def __str__(self):
        return f"Статистика по городу {self.area_name}"

    class Meta:
        verbose_name = "Статистика по городу"
        verbose_name_plural = "Статистика по городам"


class SalaryAvgAreaTop10(models.Model):
    area_name = models.CharField("Город", max_length=128, primary_key=True)
    salary_avg = models.DecimalField("Средняя з/п ", max_digits=16, decimal_places=1)

    def __str__(self):
        return f"Статистика по городу {self.area_name}"

    class Meta:
        verbose_name = "Статистика по городу"
        verbose_name_plural = "Статистика по лучшим городам"

class SalaryAvgAreaProfTop10(models.Model):
    area_name = models.CharField("Город", max_length=128, primary_key=True)
    salary_avg_prof = models.DecimalField("Средняя з/п ", max_digits=16, decimal_places=1)

    def __str__(self):
        return f"Статистика по городу {self.area_name} для профессии c#"

    class Meta:
        verbose_name = "Статистика по городу для профессии c#"
        verbose_name_plural = "Статистика по лучшим городам для профессии c#"


class VacanciesPercentAreaTop10(models.Model):
    area_name = models.CharField("Город", max_length=128, primary_key=True)
    vacancies_percent = models.DecimalField('Доля вакансий', max_digits=4, decimal_places=3)

    def __str__(self):
        return f"Доля вакансий в {self.area_name}"

    class Meta:
        verbose_name = "Доля вакансий в городе"
        verbose_name_plural = "Доли вакансий в городах"


class VacanciesPercentAreaProfTop10(models.Model):
    area_name = models.CharField("Город", max_length=128, primary_key=True)
    vacancies_percent_prof = models.DecimalField('Доля вакансий', max_digits=4, decimal_places=3)

    def __str__(self):
        return f"Доля вакансий в {self.area_name} для профессии c#"

    class Meta:
        verbose_name = "Доля вакансий в городе для профессии c#"
        verbose_name_plural = "Доли вакансий в городах для профессии c#"