from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return ("self.nombre")


class Cancha(models.Model):
    TYPE_FIELD = [
        ('P','Pasto'),
        ('B','Baby'),
        ('G','Gimnacio')
    ]

    type_field = models.CharField(
        max_length=1,
        choices=TYPE_FIELD,
        default='Pasto',
    )

    def getValue (self):
        if (self.type_field == 'P'):
            return 13000
        if (self.type_field == 'B'):
            return 10000
        else:
            return 8000

    class Meta:
        """Meta definition for Cancha."""

        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'

    def __str__(self):
        return (self.type_field)

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return(self.cancha.type_field)