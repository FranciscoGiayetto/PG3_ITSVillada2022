from django.contrib import admin

from app1.models import Article, Categoria, Producto, Venta,Direccion_cliente,Direccion_proveedor,Cliente,Proveedor,Telefonos_clientes,Producto_venta

# Register your models here.
admin.site.site_header='SUPERMERCADO'
admin.site.index_title = 'ADMIN SUPERMERCADO'
admin.site.site_title='SUPERMERCADO'

admin.site.register(Article)

class CategoriaAdmin(admin.ModelAdmin):
    list_display =['nombre','descripcion'] 
    search_fields=['nombre']
    
admin.site.register(Categoria, CategoriaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display =['nombre','precio','stock'] 
    list_filter=('nombre','precio','stock')
admin.site.register(Producto,ProductoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display =['rut','nombre','direccion','web','telefono'] 
admin.site.register(Proveedor,ProveedorAdmin)

class VentaAdmin(admin.ModelAdmin):
    list_display =('PrecioFinal')
    def PrecioFinal(self, obj):
        return Producto_venta.cantidad* Producto.precio

admin.site.register(Venta)

class Direccion_clienteAdmin(admin.ModelAdmin):
    list_display =['calle','numero','comuna','ciudad'] 
    list_filter=('calle','numero','comuna','ciudad')
admin.site.register(Direccion_cliente, Direccion_clienteAdmin)

class Direccion_proveedorAdmin(admin.ModelAdmin):
    list_display =['calle','numero','comuna','ciudad'] 
    list_filter=('calle','numero','comuna','ciudad')
admin.site.register(Direccion_proveedor, Direccion_proveedorAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display =['rut','nombre','direccion','telefono'] 
admin.site.register(Cliente, ClienteAdmin)

class Telefonos_clienteAdmin(admin.ModelAdmin):
    list_display =['telefono'] 
admin.site.register(Telefonos_clientes,Telefonos_clienteAdmin)

