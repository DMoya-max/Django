from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *

# ==========================
# INDEX
# ==========================
def index(request):
    perfil = Perfil.objects.first()
    habilidades = Habilidad.objects.all()
    lenguajes = Lenguaje.objects.all()
    proyectos = Proyecto.objects.all()
    experiencia = Experiencia.objects.all()
    estudios = Estudio.objects.all()
    hobbies = Hobby.objects.all()

    form = ContactoForm()

    return render(request, "index.html", {
        "perfil": perfil,
        "habilidades": habilidades,
        "lenguajes": lenguajes,
        "proyectos": proyectos,
        "experiencia": experiencia,
        "estudios": estudios,
        "hobbies": hobbies,
        "form": form
    })


# ==========================
# CONTACTO
# ==========================
def enviar_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
            return redirect('app:index')
    return redirect('app:index')


# ==========================
# FUNCIONES CRUD
# ==========================

def listar(request, modelo, template):
    datos = modelo.objects.all()
    campos = [f.name for f in modelo._meta.fields if f.name != "id"]
    return render(request, template, {"datos": datos, "campos": campos})


def crear(request, formulario, template, redireccion):
    form = formulario(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(redireccion)
    return render(request, template, {"form": form})


def editar(request, id, modelo, formulario, template, redireccion):
    instancia = get_object_or_404(modelo, id=id)
    form = formulario(request.POST or None, request.FILES or None, instance=instancia)
    if form.is_valid():
        form.save()
        return redirect(redireccion)
    return render(request, template, {"form": form})


def eliminar(request, id, modelo, template, redireccion):
    instancia = get_object_or_404(modelo, id=id)
    if request.method == "POST":
        instancia.delete()
        return redirect(redireccion)
    return render(request, template, {"obj": instancia})


# ---------- CRUD LISTADO ---------- #

def listar_perfil(request):
    return render(request, "perfil/listar.html", {"datos": Perfil.objects.all()})

def listar_habilidad(request):
    return render(request, "habilidades/listar.html", {"datos": Habilidad.objects.all()})

def listar_lenguaje(request):
    return render(request, "lenguajes/listar.html", {"datos": Lenguaje.objects.all()})

def listar_proyecto(request):
    return render(request, "proyectos/listar.html", {"datos": Proyecto.objects.all()})

def listar_experiencia(request):
    return render(request, "experiencia/listar.html", {"datos": Experiencia.objects.all()})

def listar_estudio(request):
    return render(request, "estudios/listar.html", {"datos": Estudio.objects.all()})

def listar_hobby(request):
    return render(request, "hobbies/listar.html", {"datos": Hobby.objects.all()})
