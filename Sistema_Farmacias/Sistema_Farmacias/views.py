from django.http import HttpResponse
# views.py
from django.http import HttpResponse
from django.shortcuts import render


def listar_clientes(request):
    return HttpResponse("Listado de clientes")


def agregar_cliente(request):
    return HttpResponse("Agregar un nuevo cliente")


def listar_pedidos(request):
    return HttpResponse("Listado de pedidos")


def agregar_pedido(request):
    return HttpResponse("Agregar un nuevo pedido")


def detalle_pedido(request, pedido_id):
    return HttpResponse(f"Detalles del pedido {pedido_id}")


def home(request):
    return render(request,"Bienvenido a Sistema Farmacias")