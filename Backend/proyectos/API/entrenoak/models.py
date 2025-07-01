from django.contrib.auth.models import AbstractUser
from django.db import models

from entrenoak.utils import TiposAlertas, TiposEstados

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to="site/logo")

    class Meta:
        verbose_name = "site"
        verbose_name_plural = "1. Site"

    def __str__(self):
        return self.name

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to = "users/avatars/%Y/%m/%d/",
        default="users/avatars/default.jpg",
    )

    bio = models.TextField(max_length = 500, null=True)
    location = models.CharField(max_length = 30, null=True)
    website = models.CharField(max_length = 100, null=True)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "2. Users"

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField()
    descripcion = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "4. Categorias"

    def __str__(self):
        return self.nombre

class Entrenamiento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    distancia = models.FloatField()
    desnivel = models.IntegerField()
    localizacion = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.IntegerField()
    recorrido = models.CharField(max_length=100)
    temperatura_max = models.FloatField()
    temperatura_min = models.FloatField()

    alerta = models.IntegerField(
        choices=TiposAlertas.choices(),
        default = TiposAlertas.SEGURO,
        blank=True,
        null=True)

    estado  =  models.IntegerField(
        choices = TiposEstados.choices(),
        default = TiposEstados.BORRADOR,
        blank=True,
        null=True
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    # desde : https://www.thedevspace.io/community/django-vue
    # Each post can receive likes from multiple users, and each user can like multiple posts
    likes = models.ManyToManyField(User, related_name = "entrenamiento_like")

    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "entrenamiento"
        verbose_name_plural = "3.Entrenamientos"
    def __str__(self):
        return self.titulo
    def get_number_of_likes(self):
        return self.likes.count()

class Corredor(models.Model):
    nickname = models.CharField(max_length=50)
    #La idea es que se puedan añadir corredores que no tengan una cuenta dentro de la plataforma.
    # Entonces la foto sería opcional y se guardaría en un directorio diferente.
    # Cuando se borre el entrenamiento, se borran las fotos de los que no tenían perfil.
    avatar = models.ImageField(
        upload_to="runners/avatars/%Y/%m/%d/",
        default="runners/avatars/default.jpg",
    )

    slug = models.SlugField()

    # Varios corredores pueden participar en multitud de entrenamientos.
    entrenamientos = models.ManyToManyField(Entrenamiento)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "corredor"
        verbose_name_plural = "5. Corredores"

    def __str__(self):
        return self.nickname

class Equipo(models.Model):
    nickname = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    descripcion = models.TextField()
    avatar = models.ImageField(
        upload_to="runners/avatars/%Y/%m/%d/",
        default="runners/avatars/default.jpg",
    )
    administrador = models.ForeignKey("User", on_delete=models.CASCADE)

    # Varios equipos pueden participar en un entrenamiento, así como, en otros entrenamientos pueden participar varios equipos.
    entrenamientos = models.ManyToManyField(Entrenamiento)
    # Varios corredores pueden participar en varios equipos.
    corredores = models.ManyToManyField(Corredor)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "equipo"
        verbose_name_plural = "6. Equipos"

    def __str__(self):
        return self.nickname
