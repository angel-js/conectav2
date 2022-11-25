from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    contrasenia = models.CharField(max_length=80)