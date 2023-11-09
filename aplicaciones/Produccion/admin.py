from django.contrib import admin
from .models import Producto

# Register your models here.
# admin.site.register(Producto)

@admin.register(Producto)
class Producto_Admin(admin.ModelAdmin):
    list_display = ('id','nombre','symbol','cantidad','code','descuento','precio')
    list_editable = ('nombre','symbol','code','cantidad','descuento','precio')
    list_display_links = ('nombre','symbol','code')
    list_filter = ('nombre',)
    list_per_page = 6

# admin.site.register(Producto, Producto_Admin)

    fieldsets=(
        (None,{
            'fields':('nombre',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('code',)
        })
    )

    def code(self,obj):
        return obj.codigo.upper()
    
    code.short_description = 'CODIGO'

    def symbol(self,obj):
        return obj.marca.upper()
    
    symbol.short_description = 'MARCA'
    symbol.empty_value_display = '???'


