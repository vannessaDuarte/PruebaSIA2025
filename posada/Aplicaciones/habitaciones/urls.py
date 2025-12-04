from django.urls import path
from . import views

urlpatterns = [
    # Lista de Habitaciones
    path('lista_habitaciones/', views.HabitacionListView.as_view(), name='lista_habitaciones'),
    # Crear Habitación
    path('crear_habitacion/', views.HabitacionCreateView.as_view(), name='crear_habitacion'),
    # Editar Habitación
    path('<int:pk>/editar_habitacion/', views.HabitacionUpdateView.as_view(), name='editar_habitacion'),
    # Eliminar Habitación
    path('<int:pk>/eliminar_habitacion/', views.HabitacionDeleteView.as_view(), name='eliminar_habitacion'),
    
    path('tipos/crear_tipo/', views.TipoHabitacionCreateView.as_view(), name='crear_tipo_habitacion'),
    path('tipos/lista_tipo/', views.TipoHabitacionListView.as_view(), name='lista_tipos_habitacion'),
    path('tipos/ajax/crear/', views.TipoHabitacionCreateAjaxView.as_view(), name='ajax_crear_tipo_habitacion'),
]