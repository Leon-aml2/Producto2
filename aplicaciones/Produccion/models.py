from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    cantidad = models.PositiveSmallIntegerField()
    codigo = models.CharField(max_length=30)
    descuento = models.PositiveSmallIntegerField()
    precio = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} (marca: {1} cantidad: {2} codigo: {3} descuento: {4} precio: {5})"
        return texto.format(self.nombre,self.marca,self.cantidad,self.codigo,self.descuento,self.precio)