from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from main.models import Drugs, Categories, Forms, Manufacturers, CountryOfOrigin, Operations


def index(request):
    checked_categories, checked_forms, checked_manufacturers, checked_country_of_origins = list(), list(), list(), list()

    if '?' in request.get_full_path():
        for parameter in request.get_full_path().split('?')[1].split('&'):
            if parameter.split('=')[0] == 'category':
                checked_categories.append(Categories.objects.filter(id=parameter.split('=')[1])[0])
            elif parameter.split('=')[0] == 'form':
                checked_forms.append(Forms.objects.filter(id=parameter.split('=')[1])[0])
            elif parameter.split('=')[0] == 'manufacturer':
                checked_manufacturers.append(Manufacturers.objects.filter(id=parameter.split('=')[1])[0])
            elif parameter.split('=')[0] == 'country_of_origin':
                checked_country_of_origins.append(CountryOfOrigin.objects.filter(id=parameter.split('=')[1])[0])

    if request.GET:
        drugs_categories = Drugs.objects.filter(category__id__in=request.GET.getlist('category'))
        drugs_forms = Drugs.objects.filter(form__id__in=request.GET.getlist('form'))
        drugs_manufacturers = Drugs.objects.filter(manufacturer__id__in=request.GET.getlist('manufacturer'))
        drugs_country_of_origin = Drugs.objects.filter(country_of_origin__id__in=request.GET.getlist('country_of_origin'))
        drugs_names = []
        if 'search' in request.GET:
            drugs_names = [drug for drug in Drugs.objects.all() if request.GET['search'] in drug.name]

        if not drugs_categories:
            drugs_categories = Drugs.objects.all()
        if not drugs_forms:
            drugs_forms = Drugs.objects.all()
        if not drugs_manufacturers:
            drugs_manufacturers = Drugs.objects.all()
        if not drugs_country_of_origin:
            drugs_country_of_origin = Drugs.objects.all()
        if not drugs_names:
            drugs_names = Drugs.objects.all()

        drugs = list(
            set(drugs_categories) & set(drugs_forms) & set(drugs_manufacturers) & set(drugs_country_of_origin) & set(
                drugs_names))
    else:
        drugs = Drugs.objects.all()

    context = {
        'drugs': drugs,
        'categories': [cat for cat in Categories.objects.all()],
        'forms': [form for form in Forms.objects.all()],
        'manufacturers': [manufacturer for manufacturer in Manufacturers.objects.all()],
        'country_of_origins': [country for country in CountryOfOrigin.objects.all()],
        'checked_categories': checked_categories,
        'checked_forms': checked_forms,
        'checked_manufacturers': checked_manufacturers,
        'checked_country_of_origins': checked_country_of_origins,
    }

    return render(request, 'index.html', context=context)


def add_drug(request):
    if request.method == 'POST':
        current_drug = Drugs.objects.create(
            name=request.POST['name'],
            price='0',
            photo=request.POST['photo'],
            is_prescription_required=True if 'is_prescription_required' in request.POST else False,
            date_of_manufacture=request.POST['date_of_manufacture'],
            service_life='1',
            description=request.POST['description'],
            number_of_drugs='1'
        )

        current_drug.category.add(Categories.objects.all()[0])
        current_drug.form.add(Forms.objects.all()[0])
        current_drug.manufacturer.add(Manufacturers.objects.all()[0])
        current_drug.country_of_origin.add(CountryOfOrigin.objects.all()[0])

        try:
            current_drug.price = float(request.POST['price'].replace(',', '.'))
            current_drug.service_life = int(request.POST['service_life'])
            current_drug.number_of_drugs = int(request.POST['number_of_drugs'])
        except ValueError:
            return HttpResponse('Введіть коректне число!')

        def update_data(field_name, model_name):
            current_data = getattr(current_drug, field_name).all()[0]
            if request.POST[field_name] != current_data:
                if request.POST[field_name] not in [obj.name for obj in model_name.objects.all()]:
                    model_name.objects.create(name=request.POST[field_name])
                [getattr(current_drug, field_name).remove(obj) for obj in getattr(current_drug, field_name).all()]
                getattr(current_drug, field_name).add(model_name.objects.filter(name=request.POST[field_name])[0])

        update_data('category', Categories)
        update_data('form', Forms)
        update_data('manufacturer', Manufacturers)
        update_data('country_of_origin', CountryOfOrigin)

        current_drug.save()

        return redirect(f'/drug_{current_drug.id}')
    if request.method == 'GET':
        return render(request, 'add_drug.html')


def delete_drug(request, drug_id, num_to_delete, price):
    current_drug = Drugs.objects.filter(id=drug_id)[0]
    if num_to_delete == 1:
        Operations.objects.create(
            description=f"Видалення 1 елементу {current_drug.name}",
            price=price,
            date_time_of_operation=timezone.now()
        )
        current_drug.number_of_drugs -= 1
        current_drug.save()
        return redirect(f'/drug_{drug_id}')
    elif num_to_delete == 0:
        Operations.objects.create(
            description=f"Видалення всіх {current_drug.name}",
            price=price,
            date_time_of_operation=timezone.now()
        )
        current_drug.delete()
        return redirect('/drugs')
    else:
        Operations.objects.create(
            description=f"Видалення {num_to_delete} елементів {current_drug.name}",
            price=price,
            date_time_of_operation=timezone.now()
        )
        current_drug.number_of_drugs -= int(num_to_delete)
        current_drug.save()
        return redirect(f'/drug_{drug_id}')


def create_order(request):
    if request.method == 'POST':
        for drug, count in zip(request.POST.getlist('chosen_drug'), request.POST.getlist('count_drug')):
            if drug != "Оберіть препарат":
                delete_drug(None, Drugs.objects.filter(name=drug)[0].id, count, request.POST['Price'])
        return redirect('/drugs')
    if request.method == 'GET':
        return render(request, 'create_order.html', context={'drugs': Drugs.objects.all()})


def drug_page(request, drug_id):
    current_drug = Drugs.objects.filter(id=drug_id)[0]

    if request.method == 'GET':
        return render(request, 'drug_info.html', context={'drug': current_drug})

    if request.method == 'POST':
        try:
            current_drug.price = float(request.POST['price'].replace(',', '.'))
            current_drug.service_life = int(request.POST['service_life'])
            current_drug.number_of_drugs = int(request.POST['number_of_drugs'])
        except ValueError:
            return HttpResponse('Введіть коректне число!')

        def update_data(field_name, model_name):
            current_data = getattr(current_drug, field_name).all()[0]
            if request.POST[field_name] != current_data:
                if request.POST[field_name] not in [obj.name for obj in model_name.objects.all()]:
                    model_name.objects.create(name=request.POST[field_name])
                [getattr(current_drug, field_name).remove(obj) for obj in getattr(current_drug, field_name).all()]
                getattr(current_drug, field_name).add(model_name.objects.filter(name=request.POST[field_name])[0])

        update_data('category', Categories)
        update_data('form', Forms)
        update_data('manufacturer', Manufacturers)
        update_data('country_of_origin', CountryOfOrigin)

        current_drug.save()

        return redirect(f'/drug_{drug_id}')


def order_history(request):
    orders = Operations.objects.all()
    orders_list = []
    order = {}
    order_drugs = []

    for counter in range(len(orders)):
        drug_info = {'name': ' '.join(orders[counter].description.split(' ')[3:]),
                     'count': orders[counter].description.split(' ')[1]}
        order_drugs.append(drug_info)

        if counter == len(orders) - 1 or counter < len(orders) - 1 and orders[counter].price != orders[counter + 1].\
                price and orders[counter].date_time_of_operation != orders[counter + 1].date_time_of_operation:
            order['drugs'] = order_drugs
            order['price'] = orders[counter].price
            order['time'] = orders[counter].date_time_of_operation
            order['id'] = orders[counter].id

            orders_list.append(order)
            order_drugs = []
            order = {}

    return render(request, 'order_history.html', context={'orders': orders_list[::-1]})
