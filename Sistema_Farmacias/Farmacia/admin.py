from django.contrib import admin
from .models import Sucursal, Cliente, Medicamento, Pedido, Venta

admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Medicamento)
admin.site.register(Pedido)
admin.site.register(Venta)
