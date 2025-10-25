from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente
from .forms import PacienteForm

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    # Ordenar todos los pacientes para obtener el índice del actual
    pacientes_ordenados = list(Paciente.objects.order_by('id'))
    index = pacientes_ordenados.index(paciente)

    # Placeholder según posición si no tiene foto
    placeholder = None
    if not paciente.foto:
        if index == 0:
            placeholder = 'img/pac.jpg'
        elif index == 1:
            placeholder = 'img/pac2.jpg'
        elif index == 2:
            placeholder = 'img/pac3.jpg'
        else:
            placeholder = 'img/pac.jpg'

    return render(request, 'detalle_paciente.html', {
        'paciente': paciente,
        'placeholder': placeholder
    })



def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_pacientes:listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'formulario_paciente.html', {'form': form, 'titulo': 'Registrar Paciente'})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('app_pacientes:detalle_paciente', paciente_id=paciente.id)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'formulario_paciente.html', {'form': form, 'titulo': 'Editar Paciente'})

def borrar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('app_pacientes:listar_pacientes')
    return render(request, 'confirmar_borrar.html', {'paciente': paciente})

def crear_cita(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.id_paciente = paciente
            cita.save()
            return redirect('app_pacientes:detalle_paciente', paciente_id=paciente.id)
    else:
        form = CitasForm()

    return render(request, 'formulario_cita.html', {
        'form': form,
        'titulo': f'Agregar cita para {paciente.nombre}'
    })

