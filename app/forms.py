from django import forms
from django.forms import ModelForm
from .models import Perfil, Habilidad, Lenguaje, Proyecto, Experiencia, Estudio, Hobby, Contacto


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = "__all__"


class HabilidadForm(ModelForm):
    class Meta:
        model = Habilidad
        fields = "__all__"


class LenguajeForm(ModelForm):
    class Meta:
        model = Lenguaje
        fields = "__all__"


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = "__all__"


class ExperienciaForm(ModelForm):
    class Meta:
        model = Experiencia
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }


class EstudioForm(ModelForm):
    class Meta:
        model = Estudio
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }


class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = "__all__"


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "mensaje"]
