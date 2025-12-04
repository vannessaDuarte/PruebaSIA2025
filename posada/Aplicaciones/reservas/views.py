from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # Para redirigir después de guardar
from .models import Reserva
from .forms import ReservaForm

# (Mantenemos la vista ReservaListView anterior)

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/crear_reserva.html'
    # La URL a donde redirigir después de crear la reserva (usamos el name de la URL)
    success_url = reverse_lazy('lista_reservas') 
    
    def form_valid(self, form):
        # Opcional: Aquí puedes agregar lógica adicional antes de guardar, 
        # como validar disponibilidad o calcular el precio_total si no viene del formulario.
        # Por ahora, solo guardamos.
        return super().form_valid(form)

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reservas/lista_reservas.html'
    context_object_name = 'reservas'
    paginate_by = 15

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('lista_reservas')

# 3. VISTA PARA ELIMINAR RESERVA (desde el listado)
class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/reserva_confirm_delete.html' # Crea este template simple
    success_url = reverse_lazy('lista_reservas')