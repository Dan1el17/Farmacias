"""
URL configuration for Sistema_Farmacias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('', views.home, name='home'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
]
