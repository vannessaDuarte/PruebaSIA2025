from django.db import models


class TipoHabitacion(models.Model):
    TIPO_CHOICES = [
        ('IND', 'Individual'),
        ('DOB', 'Doble'),
        ('SUI', 'Suite'),
        ('FAM', 'Familiar'),
    ]
    
    nombre = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.get_nombre_display()

    class Meta:
        verbose_name = "Tipo de Habitación"
        verbose_name_plural = "Tipos de Habitaciones"

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    # Relación de clave foránea con TipoHabitacion
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.PROTECT, related_name='habitaciones')
    piso = models.IntegerField()
    capacidad = models.IntegerField(default=2)

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo.get_nombre_display()})"
    
    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ['numero']