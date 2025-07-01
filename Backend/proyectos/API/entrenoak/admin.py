from django.contrib import admin

from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'email', 'joined_date')

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

class EntrenamientoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titulo',)}
    list_display = ('titulo', 'distancia', 'fecha', 'duracion', 'estado', 'categoria', 'created_at')

class CorredorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nickname',)}

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'localidad', 'administrador')



admin.site.register(Site)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Entrenamiento, EntrenamientoAdmin)
admin.site.register(Corredor, CorredorAdmin)
admin.site.register(Equipo, EquipoAdmin)
