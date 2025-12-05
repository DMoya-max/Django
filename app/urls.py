from django.urls import path
from . import views
from .models import *
from .forms import *

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("contacto/", views.enviar_mensaje, name="contacto"),

    # PERFIL
    path("perfil/", views.listar_perfil, name="perfil_listar"),
    path("perfil/crear/", lambda r: views.crear(r, PerfilForm, "perfil/crear.html", "app:perfil_listar"), name="perfil_crear"),
    path("perfil/editar/<int:id>/", lambda r, id: views.editar(r, id, Perfil, PerfilForm, "perfil/editar.html", "app:perfil_listar"), name="perfil_editar"),
    path("perfil/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Perfil, "perfil/eliminar.html", "app:perfil_listar"), name="perfil_eliminar"),

    # HABILIDADES
    path("habilidades/", views.listar_habilidad, name="habilidad_listar"),
    path("habilidades/crear/", lambda r: views.crear(r, HabilidadForm, "habilidades/crear.html", "app:habilidad_listar"), name="habilidad_crear"),
    path("habilidades/editar/<int:id>/", lambda r, id: views.editar(r, id, Habilidad, HabilidadForm, "habilidades/editar.html", "app:habilidad_listar"), name="habilidad_editar"),
    path("habilidades/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Habilidad, "habilidades/eliminar.html", "app:habilidad_listar"), name="habilidad_eliminar"),

    # LENGUAJES
    path("lenguajes/", views.listar_lenguaje, name="lenguaje_listar"),
    path("lenguajes/crear/", lambda r: views.crear(r, LenguajeForm, "lenguajes/crear.html", "app:lenguaje_listar"), name="lenguaje_crear"),
    path("lenguajes/editar/<int:id>/", lambda r, id: views.editar(r, id, Lenguaje, LenguajeForm, "lenguajes/editar.html", "app:lenguaje_listar"), name="lenguaje_editar"),
    path("lenguajes/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Lenguaje, "lenguajes/eliminar.html", "app:lenguaje_listar"), name="lenguaje_eliminar"),

    # PROYECTOS
    path("proyectos/", views.listar_proyecto, name="proyecto_listar"),
    path("proyectos/crear/", lambda r: views.crear(r, ProyectoForm, "proyectos/crear.html", "app:proyecto_listar"), name="proyecto_crear"),
    path("proyectos/editar/<int:id>/", lambda r, id: views.editar(r, id, Proyecto, ProyectoForm, "proyectos/editar.html", "app:proyecto_listar"), name="proyecto_editar"),
    path("proyectos/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Proyecto, "proyectos/eliminar.html", "app:proyecto_listar"), name="proyecto_eliminar"),

    # EXPERIENCIA
    path("experiencia/", views.listar_experiencia, name="experiencia_listar"),
    path("experiencia/crear/", lambda r: views.crear(r, ExperienciaForm, "experiencia/crear.html", "app:experiencia_listar"), name="experiencia_crear"),
    path("experiencia/editar/<int:id>/", lambda r, id: views.editar(r, id, Experiencia, ExperienciaForm, "experiencia/editar.html", "app:experiencia_listar"), name="experiencia_editar"),
    path("experiencia/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Experiencia, "experiencia/eliminar.html", "app:experiencia_listar"), name="experiencia_eliminar"),

    # ESTUDIOS
    path("estudios/", views.listar_estudio, name="estudio_listar"),
    path("estudios/crear/", lambda r: views.crear(r, EstudioForm, "estudios/crear.html", "app:estudio_listar"), name="estudio_crear"),
    path("estudios/editar/<int:id>/", lambda r, id: views.editar(r, id, Estudio, EstudioForm, "estudios/editar.html", "app:estudio_listar"), name="estudio_editar"),
    path("estudios/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Estudio, "estudios/eliminar.html", "app:estudio_listar"), name="estudio_eliminar"),

    # HOBBIES
    path("hobbies/", views.listar_hobby, name="hobby_listar"),
    path("hobbies/crear/", lambda r: views.crear(r, HobbyForm, "hobbies/crear.html", "app:hobby_listar"), name="hobby_crear"),
    path("hobbies/editar/<int:id>/", lambda r, id: views.editar(r, id, Hobby, HobbyForm, "hobbies/editar.html", "app:hobby_listar"), name="hobby_editar"),
    path("hobbies/eliminar/<int:id>/", lambda r, id: views.eliminar(r, id, Hobby, "hobbies/eliminar.html", "app:hobby_listar"), name="hobby_eliminar"),
]
