from django.contrib import admin
from .models import Comentario, Comuna, Familiar, Ficha, Funcionario, Ingreso, Paciente, Patologia, Region, Rol, Sintoma

# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_funcionario',)
    list_filter = ('id',)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_comuna',)
    list_filter = ('id','nombre_comuna',)

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('id', 'relacion_paciente', 'rut',)
    list_filter = ('id',)

class FichaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_comentario', 'id_paciente',)
    list_filter = ('id',)

class IngresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_paciente',)
    list_filter = ('id',)

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo',)
    list_filter = ('id',)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut',)
    list_filter = ('id',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_region',)
    list_filter = ('id', 'nombre_region',)


class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_rol',)
    list_filter = ('id', 'nombre_rol',)

""" class SintomaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_sintoma')
    list_filter = ('id','nombre_sintoma',)
class PatologiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_patologia')
    list_filter = ('id', 'nombre_patologia',) """


admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Patologia)
admin.site.register(Sintoma)