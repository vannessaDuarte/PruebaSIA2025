from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    # Sobrescribimos el constructor para personalizar los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Añadimos clases de Bootstrap a todos los campos para el diseño
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Opcional: Aseguramos que los campos de fecha usen el tipo 'date' de HTML5
        self.fields['fecha_entrada'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        self.fields['fecha_salida'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

        # Mejoramos el aspecto del selector de Habitaciones y Clientes
        self.fields['habitacion'].empty_label = "Seleccione una habitación"
        self.fields['cliente'].empty_label = "Seleccione un cliente"

    class Meta:
        model = Reserva
        # Los campos que queremos que aparezcan en el formulario
        fields = [
            'cliente', 
            'habitacion', 
            'fecha_entrada', 
            'fecha_salida', 
            'estado', 
            # 'precio_total' se calcularía generalmente en la vista/modelo, 
            # pero lo dejamos para ingresar manualmente por simplicidad.
            'precio_total' 
        ]