# Generated by Django 4.1.3 on 2022-11-25 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_comentario', models.DateField()),
                ('hora_comentario', models.TimeField()),
                ('estado', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Comentarios',
                'db_table': 'comentario',
                'ordering': ['id_funcionario'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Comuna',
                'db_table': 'comuna',
                'ordering': ['nombre_comuna'],
            },
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=80)),
                ('contrasenia', models.CharField(max_length=80)),
                ('relacion_paciente', models.CharField(max_length=30)),
                ('id_comuna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.comuna')),
            ],
            options={
                'verbose_name_plural': 'Familiares',
                'db_table': 'familiar',
                'ordering': ['relacion_paciente'],
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.comentario')),
            ],
            options={
                'verbose_name_plural': 'Fichas',
                'db_table': 'ficha',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=80)),
                ('contrasenia', models.CharField(max_length=80)),
                ('cargo', models.CharField(max_length=30)),
                ('id_comuna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.comuna')),
            ],
            options={
                'verbose_name_plural': 'Funcionarios',
                'db_table': 'funcionario',
                'ordering': ['cargo'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_comentario', models.DateField()),
                ('hora_comentario', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Ingresos',
                'db_table': 'ingreso',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=80)),
                ('contrasenia', models.CharField(max_length=80)),
                ('sexo_biologico', models.CharField(max_length=20)),
                ('id_comuna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.comuna')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'db_table': 'paciente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_patologia', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Patologias',
                'db_table': 'patologia',
                'ordering': ['nombre_patologia'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Regiones',
                'db_table': 'region',
                'ordering': ['nombre_region'],
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=20)),
                ('lectura', models.BooleanField(default=True)),
                ('actualizar', models.BooleanField(default=True)),
                ('borrar', models.BooleanField(default=True)),
                ('crear', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Roles',
                'db_table': 'rol',
                'ordering': ['nombre_rol'],
            },
        ),
        migrations.CreateModel(
            name='Sintoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sintoma', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'Sintomas',
                'db_table': 'sintoma',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_patologia',
            field=models.ManyToManyField(to='main_app.patologia'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.region'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rol'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.paciente'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='id_sintoma',
            field=models.ManyToManyField(to='main_app.sintoma'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='id_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.region'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rol'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='id_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ingreso'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.paciente', unique=True),
        ),
        migrations.AddField(
            model_name='familiar',
            name='id_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.region'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rol'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.region'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.funcionario'),
        ),
    ]
