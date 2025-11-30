# Importa funciones esenciales para manejar vistas, redirecciones y errores 404
from django.shortcuts import render, redirect, get_object_or_404
# Importa el sistema de mensajes de Django (para mostrar alertas en pantalla)
from django.contrib import messages
# Importa todos los modelos del proyecto
from .models import *
# Importa todos los formularios del proyecto
from .forms import *



# INDEX — Página principal del portafolio
def index(request):
    # Obtiene el primer perfil registrado (solo debería haber uno)
    perfil = Perfil.objects.first()

    # Obtiene todos los datos para mostrarlos en la página principal
    habilidades = Habilidad.objects.all()
    lenguajes = Lenguaje.objects.all()
    proyectos = Proyecto.objects.all()
    experiencia = Experiencia.objects.all()
    estudios = Estudio.objects.all()
    hobbies = Hobby.objects.all()

    # Formulario de contacto vacío para insertar en la página
    form = ContactoForm()

    # Envía todo al template index.html
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


# CONTACTO — Procesa el formulario de mensaje
def enviar_mensaje(request):
    # Valida si el formulario llegó por método POST
    if request.method == "POST":
        # Crea un formulario con los datos enviados por el usuario
        form = ContactoForm(request.POST)
        # Si el formulario es válido, se guarda en la base de datos
        if form.is_valid():
            form.save()
            # Mensaje para notificar al usuario
            messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
            # Redirige nuevamente al inicio del sitio
            return redirect('app:index')
    # Si alguien intenta acceder a contacto sin enviar un formulario, lo regresamos
    return redirect('app:index')


# CRUD — FUNCIONES GENÉRICAS (PARA REUTILIZAR EN TODOS LOS MODELOS)
def listar(request, modelo, template):
    # Obtiene todos los registros del modelo indicado (Perfil, Proyecto, etc.)
    datos = modelo.objects.all()
    # Obtiene los nombres de los campos (excepto el ID)
    campos = [f.name for f in modelo._meta.fields if f.name != "id"]
    # Carga el template correspondiente al listado
    return render(request, template, {"datos": datos, "campos": campos})


def crear(request, formulario, template, redireccion):
    # Crea un formulario vacío o con datos enviados
    form = formulario(request.POST or None, request.FILES or None)
    # Si el formulario es válido, guarda el dato en la base de datos
    if form.is_valid():
        form.save()
        # Después de crear, redirige al listado correspondiente
        return redirect(redireccion)
    # Si es GET o formulario no válido, muestra el formulario
    return render(request, template, {"form": form})


def editar(request, id, modelo, formulario, template, redireccion):
    # Busca el registro por ID o muestra error 404 si no existe
    instancia = get_object_or_404(modelo, id=id)
    # Carga el formulario con los datos existentes (para editar)
    form = formulario(request.POST or None, request.FILES or None, instance=instancia)
    # Cuando el usuario envía el formulario
    if form.is_valid():
        form.save()
        return redirect(redireccion)
    # Si es GET, muestra el formulario con los datos cargados
    return render(request, template, {"form": form})


def eliminar(request, id, modelo, template, redireccion):
    # Busca el registro que se desea borrar
    instancia = get_object_or_404(modelo, id=id)
    # Si el usuario confirma la eliminación con POST
    if request.method == "POST":
        instancia.delete()
        return redirect(redireccion)
    # Muestra la página de confirmación de eliminación
    return render(request, template, {"obj": instancia})



# CRUD LISTADOS DIRECTOS (PARA USAR EN LAS URLS SIN INCLUIR LÓGICA EXTRA)
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
