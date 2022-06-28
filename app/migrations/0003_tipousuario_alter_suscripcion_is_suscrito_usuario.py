# Generated by Django 4.0.4 on 2022-06-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_despacho_fecha_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_usuario',
            },
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='is_suscrito',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipousuario')),
            ],
            options={
                'db_table': 'db_usuario',
            },
        ),
    ]
