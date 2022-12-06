# Generated by Django 2.2.2 on 2022-05-11 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_continente', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Motivacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_motivacion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=45)),
                ('continente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Continente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipodocumento', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Turista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('a_paterno', models.CharField(max_length=25)),
                ('a_materno', models.CharField(max_length=25)),
                ('genero', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO'), ('OTRO', 'OTRO')], max_length=25)),
                ('edad', models.IntegerField()),
                ('profesion', models.CharField(max_length=125)),
                ('nacionalidad', models.CharField(max_length=125)),
                ('modalidad_viaje', models.CharField(choices=[('INDIVIDUAL', 'INDIVIDUAL'), ('GRUPO', 'GRUPO')], max_length=15)),
                ('duracion_estadia', models.IntegerField()),
                ('gasto_diario', models.FloatField()),
                ('observaciones', models.CharField(max_length=125)),
                ('procedencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Pais')),
                ('tipodocumento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.TipoDocumento')),
            ],
        ),
        migrations.CreateModel(
            name='TuristaHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Hotel')),
                ('turista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Turista')),
            ],
        ),
        migrations.CreateModel(
            name='MotivacionTurista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Motivacion')),
                ('turistahotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.TuristaHotel')),
            ],
        ),
    ]
