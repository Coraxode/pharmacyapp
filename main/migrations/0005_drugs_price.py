# Generated by Django 4.2.1 on 2023-05-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_drugs_type_drugs_category_drugs_form_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='price',
            field=models.FloatField(blank=True, default=0, help_text='Ціна'),
        ),
    ]