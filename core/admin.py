from django.contrib import admin
from .models import *

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

