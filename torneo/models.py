from django.db import models
from django.contrib import admin
from PIL import Image

class Personaje(models.Model):
    nombre = models.CharField(max_length=30,default='')
    compania = models.CharField(max_length=30,default='')
    anio = models.IntegerField()
    imagen = models.ImageField(default='')

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=60)
    anio = models.IntegerField()
    consola = models.CharField(max_length=60,default='')
    personajes = models.ManyToManyField(Personaje, through='Mains')

    def __str__(self):
        return self.nombre

class Mains(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

class MainsInLine(admin.TabularInline):
    model = Mains

    extra = 1

class PersonajeAdmin(admin.ModelAdmin):
    inlines = (MainsInLine,)

class JugadorAdmin(admin.ModelAdmin):
    inlines = (MainsInLine,)
