from django.urls import path
from . import views # Importa la vista home_view si está en el mismo nivel

urlpatterns = [
    path('', views.home_view, name='home'),
]