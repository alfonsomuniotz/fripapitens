from django.contrib import admin
from .models import Usuario,Rol,Carrito,Categoria,Producto,Venta
# Register your models here.



admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Rol)
