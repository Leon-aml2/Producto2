from django.urls import path
from aplicaciones.Produccion.views import ProductoListView, delete_product, register_product, update_product

urlpatterns = [
    path('',ProductoListView.as_view(), name = 'gestion_productos'),
    path('delete_product/<int:id>', delete_product),
    path('register_product/', register_product),
    path('update_product/<int:id>', update_product),
]
