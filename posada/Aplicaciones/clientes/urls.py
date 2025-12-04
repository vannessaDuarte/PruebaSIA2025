from django.urls import path
from . import views

urlpatterns = [
    # Lista de Clientes
    path('lista_cliente/', views.ClienteListView.as_view(), name='lista_clientes'),
    # Crear Cliente
    path('crear_cliente/', views.ClienteCreateView.as_view(), name='crear_cliente'),
    # Editar Cliente
    path('<int:pk>/editar_cliente/', views.ClienteUpdateView.as_view(), name='editar_cliente'),
    # Eliminar Cliente
    path('<int:pk>/eliminar_cliente/', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),
]