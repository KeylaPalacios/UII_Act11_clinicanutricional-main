from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del paciente")
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fechanacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='pacientes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Citas(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ])
    observaciones = models.TextField(blank=True, null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')

    def __str__(self):
        return f"Cita de {self.id_paciente.nombre} el {self.fecha} a las {self.horario}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
