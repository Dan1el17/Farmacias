from django.db import models
from datetime import date


class EstadoPago(models.TextChoices):
    TARJETA = 'TARJETA', 'Tarjeta'
    EFECTIVO = 'EFECTIVO', 'Efectivo'
    TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'


class Sucursal(models.Model):
    #Atributos
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    inventario = models.ManyToManyField("Medicamento", related_name="sucursales")

    #Metodos
    def obtener_inventario(self):
        return self.inventario.all()

    def buscar_medicamento(self, nombre):
        return self.inventario.filter(nombre__icontains=nombre)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    #Atributos
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)

class Meta:
    abstract = True

    def __str__(self):
        return self.nombre


class Cliente(Persona):
    # Atributos
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name="cliente_relate")
    direccion_envio = models.CharField(max_length=255)

    # Métodos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rol = None

    def realizar_pedido(self, pedido):
        # Lógica para realizar un pedido
        print(f"{self.nombre} ha realizado un pedido: {pedido}")

    def obtener_pedido(self, pedido_id):
        # Lógica para obtener detalles de un pedido
        print(f"Detalles del pedido con ID {pedido_id}")

    def cancelar_pedido(self, pedido_id):
        # Lógica para cancelar un pedido
        print(f"Pedido con ID {pedido_id} cancelado")

    def __str__(self):
        return f"{self.nombre} ({self.rol if self.rol else 'Sin rol'})"



class Empleado(Persona):
        rol = models.CharField(max_length=20)
        sucursal_id = models.CharField(max_length=100)

        def __str__(self):
            return f"Empleado: {self.nombre}, Rol: {self.rol}"


class Medicamento(models.Model):
        #Atributos
        medicamento_id = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        sucursal = models.ManyToManyField(Sucursal, related_name="medicamentos")

        #Metodos
        def actualizar_cantidad(self):
            pass

        def entregar(self):
            pass

        def __str__(self):
            return self.nombre

class Pedido(models.Model):
        estado = models.CharField(
            max_length=20,
            choices=EstadoPago.choices,
            default=EstadoPago.EFECTIVO
        )
        cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        sucursal_id = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
        id = models.CharField(max_length=100, primary_key=True)

        def calcular_total(self):
            pass

        def __str__(self):
            return f"Pedido {self.id}"

class Venta(models.Model):
        pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
        fecha_venta = models.DateField(default=date.today)
        monto = models.FloatField()

        def procesar_venta(self):
            pass

        def cancelar_venta(self):
            pass

        def __str__(self):
            return
