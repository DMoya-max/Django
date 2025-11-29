from django.db import models

# Modelos de la app (Base de datos)
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    github = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    TIPO_SKILL = [
        ("tecnica", "Técnica"),
        ("blanda", "Blanda"),
    ]
    SENIORITY = [
        ("junior", "Junior"),
        ("semi", "Semi-senior"),
        ("senior", "Senior"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_SKILL)
    nivel = models.CharField(max_length=20, choices=SENIORITY)

    def __str__(self):
        return self.nombre

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=Habilidad.SENIORITY)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

class Estudio(models.Model):
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo

class Hobby(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
