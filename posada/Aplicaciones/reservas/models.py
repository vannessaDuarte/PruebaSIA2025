from django.db import models

# Importamos los modelos de las otras aplicaciones
from Aplicaciones.clientes.models import Cliente
from Aplicaciones.habitaciones.models import Habitacion

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('PEN', 'Pendiente'),
        ('CON', 'Confirmada'),
        ('CAN', 'Cancelada'),
        ('COM', 'Completada'),
    ]

    # Clave Foránea al modelo Cliente (de la app clientes)
    cliente = models.ForeignKey('Cliente',  related_name='reservas')
    # Clave Foránea al modelo Habitacion (de la app habitaciones)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT, related_name='reservas')
    
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PEN')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reserva {self.id}: {self.cliente} en H. {self.habitacion.numero}"

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['-fecha_reserva']
