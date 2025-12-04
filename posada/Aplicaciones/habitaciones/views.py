from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse # Para devolver respuestas JSON
from django.views.decorators.csrf import csrf_exempt # ¡Solo para pruebas, usa CSRF token en producción!
from django.utils.decorators import method_decorator
from .models import *
from .forms import *


class HabitacionCreateView(CreateView):
    model = Habitacion
    form_class = HabitacionForm 
    template_name = 'habitaciones/habitacion_form.html'
    success_url = reverse_lazy('lista_habitaciones') # Redirige a la lista después de guardar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['tipo_form_modal'] = TipoHabitacionForm() 
        
        return context



class HabitacionListView(ListView):
    """Muestra la lista de todas las habitaciones físicas."""
    model = Habitacion
    template_name = 'habitaciones/lista_habitaciones.html'
    context_object_name = 'habitaciones'
    paginate_by = 10 


class HabitacionUpdateView(UpdateView):
    """Permite actualizar los datos de una habitación."""
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'habitaciones/habitacion_form.html'
    success_url = reverse_lazy('lista_habitaciones')

class HabitacionDeleteView(DeleteView):
    """Permite eliminar una habitación."""
    model = Habitacion
    template_name = 'habitaciones/habitacion_confirm_delete.html'
    success_url = reverse_lazy('lista_habitaciones')

# VISTA PARA CREAR TIPO DE HABITACIÓN
class TipoHabitacionCreateView(CreateView):
    model = TipoHabitacion
    form_class = TipoHabitacionForm
    template_name = 'habitaciones/tipo_habitacion_form.html'
    success_url = reverse_lazy('crear_habitacion') # Redirige a la nueva lista

# Vista para manejar la creación de TipoHabitacion por AJAX
@method_decorator(csrf_exempt, name='dispatch') # Para simplificar la prueba de POST
class TipoHabitacionCreateAjaxView(TipoHabitacionCreateView):
    
    def post(self, request, *args, **kwargs):
        form = TipoHabitacionForm(request.POST)
        
        if form.is_valid():
            # Guarda el nuevo TipoHabitacion
            instance = form.save()
            
            # Devuelve una respuesta JSON con el ID y el nombre del nuevo tipo
            return JsonResponse({
                'status': 'success',
                'id': instance.pk,
                'nombre': instance.nombre,
            })
        
        # Si la validación falla, devuelve los errores
        return JsonResponse({
            'status': 'error',
            'errors': form.errors,
        }, status=400) # Código de error 400 Bad Request
    
# VISTA PARA LISTAR TIPOS DE HABITACIÓN (Opcional, pero bueno tenerla)
class TipoHabitacionListView(ListView):
    model = TipoHabitacion
    template_name = 'habitaciones/lista_tipos_habitacion.html'
    context_object_name = 'tipos_habitacion'
    paginate_by = 10
