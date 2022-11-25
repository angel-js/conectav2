from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_region = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'region'

class Comuna(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_region = models.CharField(max_length=35)
    id_region = models.OneToOneField('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


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
    id_region = models.OneToOneField('Region', models.DO_NOTHING, db_column='id_region')
    id_comuna = models.OneToOneField('Comuna', models.DO_NOTHING, db_column='id_comuna')

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
    id_patologia = models.ManyToOne('Patologia', models.DO_NOTHING, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'

class Patologia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_patologia = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'patologia'

class Ingreso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_sintoma = models.ManyToOne('Sintoma', models.DO_NOTHING, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso'

class Sintoma(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_sintoma = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'sintomas'

class Familiar(Usuario):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    relacion_paciente = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'familiar'


class Funcionario(Usuario):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cargo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Ficha(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_comentario = models.ForeignKey(Comentario, models.DO_NOTHING, db_column='id_comentario')
    id_ingreso = models.ForeignKey('Ingreso', models.DO_NOTHING, db_column='id_ingresos')
    id_paciente = models.ForeignKey('Paciente',  models.DO_NOTHING, db_column='id_paciente', unique=True )

    class Meta:
        managed = False
        db_table = 'ficha'

class Comentario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha_comentario = models.DateField()
    hora_comentario = models.TimeField()
    estado = models.CharField(db_column='Estado', max_length=20)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=300)  # Field name made lowercase.
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario')

    class Meta:
        managed = False
        db_table = 'comentario'