from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Añade la clase 'form-control' de Bootstrap a todos los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'dni']
        labels = {
            'dni': 'Documento de Identidad (DNI)',
        }