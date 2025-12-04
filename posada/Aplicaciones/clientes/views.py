from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm # Asumiendo que tienes un ClienteForm

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm 
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('lista_clientes') # Redirige a la lista después de guardar

# (Asegúrate de tener también la ClienteListView)
class ClienteListView(ListView):
    """Muestra la lista de todos los clientes registrados."""
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'
    paginate_by = 20 # Paginación opcional

class ClienteUpdateView(UpdateView):
    """Permite actualizar los datos de un cliente."""
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'
    success_url = reverse_lazy('lista_clientes')

class ClienteDeleteView(DeleteView):
    """Permite eliminar un cliente."""
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('lista_clientes')