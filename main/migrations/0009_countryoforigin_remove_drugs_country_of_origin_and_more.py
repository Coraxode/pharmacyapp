# Generated by Django 4.2.1 on 2023-05-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_manufacturers_remove_drugs_manufacturer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryOfOrigin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='drugs',
            name='country_of_origin',
        ),
        migrations.AddField(
            model_name='drugs',
            name='country_of_origin',
            field=models.ManyToManyField(blank=True, help_text='Країна-виробник', to='main.countryoforigin'),
        ),
    ]
