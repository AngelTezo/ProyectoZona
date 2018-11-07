from django.contrib import admin
from .models import Personaje, PersonajeAdmin, Jugador, JugadorAdmin

#Registramos nuestras clases principales.
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Jugador, JugadorAdmin)
