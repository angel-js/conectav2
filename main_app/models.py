from django.db import models

# Create your models here.
class Region(models.Model):
    nombre_region = models.CharField(max_length=35)

    class Meta:
        db_table = 'region'
        verbose_name_plural = "Regiones"
        ordering= ["nombre_region"]

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=35)
    id_region = models.OneToOneField('Region', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comuna'
        verbose_name_plural = "Comuna"
        ordering= ["nombre_comuna"]


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=20)
    lectura = models.BooleanField(default=True) # This field type is a guess.
    actualizar = models.BooleanField(default=True)  # This field type is a guess.
    borrar = models.BooleanField(default=True)  # This field type is a guess.
    crear = models.BooleanField(default=True)  # This field type is a guess. 

    class Meta:
        db_table = 'rol'
        verbose_name_plural = "Roles"
        ordering= ["nombre_rol"]


class Persona(models.Model):
    rut = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    id_region = models.ManyToManyField('Region') #on_delete=models.CASCADE)
    id_comuna = models.ManyToManyField('Comuna') #on_delete=models.CASCADE)

    class Meta:
        db_table = 'persona'
        abstract = True
        verbose_name_plural = "Comunas"
        ordering= ["rut"]


class Usuario(Persona):
    email = models.CharField(max_length=80)
    contrasenia = models.CharField(max_length=80)

    class Meta:
        db_table = 'usuario'
        abstract = True
        verbose_name_plural = "Usuarios"
        ordering= ["email"]

class Paciente(Persona):
    sexo_biologico = models.CharField(max_length=20)
    id_patologia = models.ManyToManyField('Patologia')

    class Meta:
        db_table = 'paciente'
        verbose_name_plural = "Pacientes"
        ordering= ["id"]

class Patologia(models.Model):
    nombre_patologia = models.CharField(max_length=35)

    class Meta:
        db_table = 'patologia'
        verbose_name_plural = "Patologias"
        ordering= ["nombre_patologia"]


class Ingreso(models.Model):
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    id_sintoma = models.ManyToManyField('Sintoma')

    class Meta:
        db_table = 'ingreso'
        verbose_name_plural = "Ingresos"
        ordering= ["id"]


class Sintoma(models.Model):
    nombre_sintoma = models.CharField(max_length=35)

    class Meta:
        db_table = 'sintoma'
        verbose_name_plural = "Sintomas"
        ordering= ["id"]

class Familiar(Usuario):
    relacion_paciente = models.CharField(max_length=30)
    id_paciente = models.OneToOneField('Paciente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'familiar'
        verbose_name_plural = "Familiares"
        ordering= ["relacion_paciente"]


class Funcionario(Usuario):
    cargo = models.CharField(max_length=30)

    class Meta:
        db_table = 'funcionario'
        verbose_name_plural = "Funcionarios"
        ordering= ["cargo"]



class Ficha(models.Model):
    id_comentario = models.ForeignKey('Comentario', on_delete=models.CASCADE, null=True)
    id_ingreso = models.ForeignKey('Ingreso', on_delete=models.CASCADE, null=True)
    id_paciente = models.OneToOneField('Paciente',  on_delete=models.CASCADE)

    class Meta:
        db_table = 'ficha'
        verbose_name_plural = "Fichas"
        ordering= ["id"]

class Comentario(models.Model):
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    estado = models.CharField(max_length=20)  # Field name made lowercase.
    comentario = models.CharField( max_length=300)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comentario'
        verbose_name_plural = "Comentarios"
        ordering= ["id_funcionario"]
