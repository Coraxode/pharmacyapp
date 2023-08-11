from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('drugs', views.index, name='drugs'),
    path('action/delete_drug_<int:drug_id>/<int:num_to_delete>', views.delete_drug, name='delete_drug'),
    path('action/change_drug_<int:drug_id>', views.drug_page, name='change_drug_info'),
    path('drug_<int:drug_id>', views.drug_page, name='drug_page'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('add_drug/', views.add_drug, name='add_drug')
]
