from django.contrib import admin

from app1.models import Categoria, Producto, Venta,Direccion_cliente,Direccion_proveedor,Cliente,Proveedor,Telefonos_clientes,Producto_venta

# Register your models here.
search_fields=[Categoria.nombre]

admin.site.register(Categoria)
admin.site.register(Producto_venta)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(Direccion_cliente)
admin.site.register(Direccion_proveedor)
admin.site.register(Cliente)
admin.site.register(Telefonos_clientes)

