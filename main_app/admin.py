from django.contrib import admin
from .models import Comentario, Comuna, Familiar, Ficha, Funcionario, Ingreso, Paciente, Patologia, Region, Rol, Sintomas, Usuario

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Comuna)
admin.site.register(Familiar)
admin.site.register(Ficha)
admin.site.register(Funcionario)
admin.site.register(Ingreso)
admin.site.register(Paciente)
admin.site.register(Patologia)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Sintomas)
admin.site.register(Usuario)