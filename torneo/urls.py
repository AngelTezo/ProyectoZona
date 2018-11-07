from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.jugador_list, name='list'),
    url(r'^torneo/jugador/listar/$', views.jugador_list, name='jugador_list'),
    url(r'^torneo/jugador/agregar$', views.jugador_nuevo, name='jugador_nuevo'),
    url(r'^torneo/jugador/editar/(?P<pk>[0-9]+)$', views.jugador_edit, name='jugador_edit'),
    url(r'^torneo/jugador/detalles/(?P<pk>[0-9]+)$', views.jugador_details, name='jugador_details'),    
    url(r'^torneo/jugador/eliminar/(?P<pk>[0-9]+)$', views.jugador_delete, name='jugador_delete'),    
    url(r'^torneo/personaje/listar/$', views.personaje_list, name='personaje_list'),
    url(r'^torneo/personaje/agregar$', views.personaje_nuevo, name='personaje_nuevo'),
    url(r'^torneo/personaje/editar/(?P<pk>[0-9]+)$', views.personaje_edit, name='personaje_edit'),
    url(r'^torneo/personaje/detalles/(?P<pk>[0-9]+)$', views.personaje_details, name='personaje_details'),
    url(r'^torneo/personaje/eliminar/(?P<pk>[0-9]+)$', views.personaje_delete, name='personaje_delete'),

    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)