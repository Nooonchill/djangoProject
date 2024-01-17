from django.db import models

class Person(models.Model):
    first_name = models.CharField("Имя", max_length=64)
    last_name = models.CharField("Фамилия", max_length=64)
    age = models.IntegerField("Возраст")
    job = models.CharField("Должность", max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


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

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

class FormedVacancy(models.Model):
    name = models.CharField("Название", max_length=256)
    area_name = models.CharField("Город", max_length=128)
    salary = models.DecimalField("Зарплата", max_digits=16, decimal_places=1, null=True)
    date = models.CharField("Дата публикации", max_length=10, null=True)

    class Meta:
        verbose_name = "Форматированная вакансия"
        verbose_name_plural = "Форматированные вакансии"