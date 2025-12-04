from django import forms
from .models import TipoHabitacion, Habitacion

class TipoHabitacionForm(forms.ModelForm):
    """
    Formulario para crear o editar la definición de un Tipo de Habitación 
    (ej: Doble, Suite) y su precio base.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica la clase Bootstrap a todos los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
    class Meta:
        model = TipoHabitacion
        fields = ['nombre', 'descripcion', 'precio_base']
        labels = {
            'nombre': 'Tipo (Ej: Doble, Suite)',
            'precio_base': 'Precio Base por Noche',
            'descripcion': 'Características (Opcional)',
        }


class HabitacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Opcional: Mejorar la etiqueta de la clave foránea
        self.fields['tipo'].empty_label = "Seleccione un tipo de habitación"
            
    class Meta:
        model = Habitacion
        fields = ['numero', 'tipo', 'piso', 'capacidad']
        labels = {
            'numero': 'Número de Habitación',
            'tipo': 'Tipo de Habitación (Ej: Doble)',
        }