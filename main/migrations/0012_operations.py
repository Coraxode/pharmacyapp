# Generated by Django 4.2.1 on 2023-05-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_operations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Опис')),
                ('price', models.FloatField(blank=True, help_text='Ціна')),
                ('date_time_of_operation', models.DateTimeField(blank=True, help_text='Дата виготовлення')),
            ],
        ),
    ]
