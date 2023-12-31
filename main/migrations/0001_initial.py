# Generated by Django 4.2.1 on 2023-05-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Назва препарату', max_length=100)),
                ('type', models.CharField(blank=True, help_text='Тип препарату (сироп, таблетки і т.д.)', max_length=100)),
                ('manufacturer', models.CharField(blank=True, help_text='Виробник препарату', max_length=100)),
                ('country_of_origin', models.CharField(blank=True, help_text='Країна-виробник', max_length=20)),
                ('is_prescription_required', models.BooleanField(blank=True, default=False, help_text='Чи потрібен рецепт для покупки (Так/Ні)')),
                ('date_of_manufacture', models.DateField(blank=True, help_text='Дата виготовлення')),
                ('service_life', models.IntegerField(blank=True, help_text='Термін придатності (в місяцях)')),
                ('description', models.TextField(blank=True, help_text='Опис')),
            ],
        ),
    ]
