# Generated by Django 4.2.1 on 2023-05-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_forms_remove_drugs_form_drugs_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='drugs',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='drugs',
            name='manufacturer',
            field=models.ManyToManyField(blank=True, help_text='Виробник препарату', to='main.manufacturers'),
        ),
    ]
