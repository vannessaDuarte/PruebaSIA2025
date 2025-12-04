from django.urls import path
from . import views

urlpatterns = [
    # READ: Lista de reservas (con filtros)
    path('listar/', views.ReservaListView.as_view(), name='lista_reservas'), 
    
    # CREATE: Agregar nuevas reservas
    path('crear/', views.ReservaCreateView.as_view(), name='crear_reserva'),

    # UPDATE: Actualizar una reserva específica (se necesita el ID/pk)
    path('<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='editar_reserva'),
    
    # DELETE: Eliminar una reserva específica (se necesita el ID/pk)
    path('<int:pk>/eliminar/', views.ReservaDeleteView.as_view(), name='eliminar_reserva'),
]