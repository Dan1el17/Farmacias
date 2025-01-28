from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Pedido, Venta, Medicamento
from .forms import PedidoForm, ClienteForm
from django.http import HttpResponse


# Vista para listar todos los clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/listar_clientes.html', {'clientes': clientes})

# Vista para agregar un nuevo cliente
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gestion/agregar_cliente.html', {'form': form})

# Vista para listar todos los pedidos
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'gestion/listar_pedidos.html', {'pedidos': pedidos})


# Vista para agregar un nuevo pedido
def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'gestion/agregar_pedido.html', {'form': form})

# Vista para ver los detalles de un pedido
def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'gestion/detalle_pedido.html', {'pedido': pedido})

def home(request):
    return render(request,"¡Bienvenido a Sistema de Farmacias!")