from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_region = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_rol = models.CharField(max_length=20)
    lectura = models.BooleanField() # This field type is a guess.
    escritura = models.BooleanField()  # This field type is a guess.
    borrar = models.BooleanField()  # This field type is a guess.
    crear = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol'

class Persona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rut = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    contrasenia = models.CharField(max_length=80)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol', default=3)
    id_comuna = models.OneToOneField(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'persona'
        abstract = True

class Usuario(Persona):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=80)
    contrasenia = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'usuario'
        abstract = True

class Paciente(Persona):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sexo_biologico = models.CharField(max_length=20)
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario')
    
    id_sintoma = models.OneToOneField('Sintomas', models.DO_NOTHING, db_column='id_sintoma')

    class Meta:
        managed = False
        db_table = 'paciente'

class Familiar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relacion_paciente = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'familiar'


class Funcionario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'funcionario'