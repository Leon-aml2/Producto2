from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Producto
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     # return HttpResponse("<h1>Hola Mundo</h1>")
#     productos_listados =Producto.objects.all().order_by('nombre','marca')
#     # productos_listados =Producto.objects.all()[:5]
#     return render(request, "gestion_productos.html", {'productos':productos_listados})

def home(request):
    # return HttpResponse("<h1>Hola Mundo</h1>")
    productos_listados =Producto.objects.all().order_by('nombre','marca')
    # productos_listados =Producto.objects.all()[:5]
    data = {
        'titulo':'Produccion',
        'productos': productos_listados
    }
    return render(request, "gestion_productos.html", data)

class ProductoListView(ListView):
    model = Producto
    template_name = "gestion_productos.html"

    def get_queryset(self):
        return Producto.objects.all()
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = "Produccion"
        return context
    
def delete_product(request,id):
    merma = Producto.objects.get(id=id)
    merma.delete()

    return redirect('/')

def update_product(request,id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('txtNombre', producto.nombre)
        producto.marca = request.POST.get('txtMarca', producto.marca)
        producto.codigo = request.POST.get('txtCodigo', producto.codigo)
        producto.cantidad = request.POST.get('numCantidad', producto.cantidad)
        producto.descuento = request.POST.get('numDescuento', producto.descuento)
        producto.precio = request.POST.get('numPrecio', producto.precio)
        producto.save()

        return redirect('/')


def register_product(request):
    nombre = request.POST['txtNombre']
    marca = request.POST['txtMarca']
    codigo = request.POST['txtCodigo']
    cantidad = request.POST['numCantidad']
    descuento = request.POST['numDescuento']
    precio = request.POST['numPrecio']

    producto = Producto.objects.create(nombre = nombre,marca= marca,codigo=codigo,cantidad= cantidad,descuento=descuento,precio= precio)

    return redirect('/')