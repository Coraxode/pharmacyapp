from django.contrib import admin
from main.models import Drugs, Categories, Forms, Manufacturers, CountryOfOrigin, Operations

admin.site.register(Drugs)
admin.site.register(Categories)
admin.site.register(Forms)
admin.site.register(Manufacturers)
admin.site.register(CountryOfOrigin)
admin.site.register(Operations)
