# Generated by Django 4.0.1 on 2022-01-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_lanzamiento', models.DateField()),
                ('nombre_album', models.CharField(max_length=40)),
                ('canciones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_banda', models.CharField(max_length=40)),
                ('nacimiento_banda', models.DateField()),
                ('ubicacion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Biografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicios', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=40)),
                ('links_banda', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrantes', models.CharField(max_length=40)),
                ('especializacion', models.CharField(max_length=40)),
            ],
        ),
    ]