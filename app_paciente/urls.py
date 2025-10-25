from django.urls import path
from . import views

app_name = 'app_pacientes'

urlpatterns = [
    path('', views.listar_pacientes, name='listar_pacientes'),
    path('paciente/<int:paciente_id>/', views.detalle_paciente, name='detalle_paciente'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('borrar/<int:paciente_id>/', views.borrar_paciente, name='borrar_paciente'),
]
