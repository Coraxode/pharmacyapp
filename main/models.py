from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Forms(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CountryOfOrigin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Drugs(models.Model):
    name = models.CharField(max_length=100, help_text="Назва препарату")
    price = models.FloatField(help_text="Ціна",default=0, blank=True)
    category = models.ManyToManyField(Categories, help_text="Категорія препарату (протизастудні, знеболюючі і т.д.)", blank=True)
    form = models.ManyToManyField(Forms, help_text="Форма випуску препарату (сироп, таблетки і т.д.)", blank=True)
    photo = models.TextField(help_text="Фото препарату", default='', blank=True)
    manufacturer = models.ManyToManyField(Manufacturers, help_text="Виробник препарату", blank=True)
    country_of_origin = models.ManyToManyField(CountryOfOrigin, help_text="Країна-виробник", blank=True)
    is_prescription_required = models.BooleanField(default=False, help_text="Чи потрібен рецепт для покупки (Так/Ні)", blank=True)
    date_of_manufacture = models.DateField(help_text="Дата виготовлення", blank=True)
    service_life = models.IntegerField(help_text="Термін придатності (в місяцях)", blank=True)
    description = models.TextField(help_text="Опис", blank=True)
    number_of_drugs = models.IntegerField(help_text="Кількість препарату", default=0, blank=True)

    def __str__(self):
        return f'{self.name}'


class Operations(models.Model):
    description = models.TextField(help_text="Опис", blank=True)
    price = models.FloatField(help_text="Ціна", blank=True)
    date_time_of_operation = models.DateTimeField(help_text="Дата операції", blank=True)

    def __str__(self):
        return f'{self.description} на суму {self.price}'
