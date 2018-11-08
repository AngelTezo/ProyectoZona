from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import JugadorForm, PForm     
from .models import Jugador, Personaje, Mains
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def jugador_list(request):
    posts = Jugador.objects.all()
    return render(request, 'jugadores/jugador_list.html', {'posts': posts})

@login_required
def jugador_details(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    mains = Mains.objects.filter(jugador=pk)
    return render(request, 'jugadores/jugador_details.html', {'jugador': jugador, 'mains': mains })
    
@login_required
def jugador_nuevo(request):
    if request.method == "POST":
        formulario = JugadorForm(request.POST)
        if formulario.is_valid():
            jugador = Jugador.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for personaje_id in request.POST.getlist('personajes'):
                mains = Mains(personaje_id=personaje_id, jugador_id = jugador.id)
                mains.save()
            messages.add_message(request, messages.SUCCESS, 'Jugador Guardado Exitosamente')
            return redirect('jugador_list')
    else:
        formulario = JugadorForm()
    return render(request, 'jugadores/editar.html', {'formulario': formulario})

@login_required
def jugador_edit(request, pk):
    post = get_object_or_404(Jugador, pk=pk)
    if request.method == "POST":
        form = JugadorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            for personaje_id in request.POST.getlist('personajes'):
                mains = Mains(personaje_id=personaje_id, jugador_id = pk)
            for personaje_id in request.POST.getlist('personajes'):
                mains = Mains(personaje_id=personaje_id, jugador_id = pk)
                mains.save()
            post.save()
            return redirect('jugador_list')
    else:
        form = JugadorForm(instance=post)
    return render(request, 'jugadores/agregar.html', {'form': form})

@login_required
def jugador_delete(request, pk):
    post = get_object_or_404(Jugador, pk=pk)
    post.delete()
    return redirect('jugador_list')

@login_required
def personaje_nuevo(request):
    if request.method == "POST":
        formulario = PForm(request.POST)
        if formulario.is_valid():
            personaje = Personaje.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            messages.add_message(request, messages.SUCCESS, 'Jugador Guardado Exitosamente')
            return redirect('personaje_list')
    else:
        formulario = PForm()
    return render(request, 'jugadores/editar.html', {'formulario': formulario})
@login_required
def personaje_list(request):
    posts = Personaje.objects.all()
    return render(request, 'jugadores/personaje_list.html', {'posts': posts})

@login_required
def personaje_edit(request, pk):
    post = get_object_or_404(Personaje, pk=pk)
    if request.method == "POST":
        form = PForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('personaje_list')
    else:
        form = PForm(instance=post)
    return render(request, 'jugadores/agregar.html', {'form': form})

@login_required
def personaje_details(request, pk):
    post = get_object_or_404(Personaje, pk=pk)
    mains = Mains.objects.filter(personaje=pk)
    return render(request, 'jugadores/personaje_details.html', {'post': post,'mains': mains})

@login_required
def personaje_delete(request, pk):
    post = get_object_or_404(Personaje, pk=pk)
    post.delete()
    return redirect('personaje_list')