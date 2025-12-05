from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *

# ============================================
# INDEX (PORTAFOLIO PRINCIPAL)
# ============================================
def index(request):
    return render(request, "index.html", {
        "perfil": Perfil.objects.first(),
        "habilidades": Habilidad.objects.all(),
        "lenguajes": Lenguaje.objects.all(),
        "proyectos": Proyecto.objects.all(),
        "experiencia": Experiencia.objects.all(),
        "estudios": Estudio.objects.all(),
        "hobbies": Hobby.objects.all(),
        "form": ContactoForm(),
    })


# ============================================
# CONTACTO
# ============================================
def enviar_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
    return redirect("app:index")


# ============================================
# CRUD GENÉRICO
# ============================================
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


# ============================================
# LISTADOS PERSONALIZADOS
# ============================================
def listar_perfil(request):
    return listar(request, Perfil, "perfil/listar.html")

def listar_habilidad(request):
    return listar(request, Habilidad, "habilidades/listar.html")

def listar_lenguaje(request):
    return listar(request, Lenguaje, "lenguajes/listar.html")

def listar_proyecto(request):
    return listar(request, Proyecto, "proyectos/listar.html")

def listar_experiencia(request):
    return listar(request, Experiencia, "experiencia/listar.html")

def listar_estudio(request):
    return listar(request, Estudio, "estudios/listar.html")

def listar_hobby(request):
    return listar(request, Hobby, "hobbies/listar.html")
