# Generated by Django 4.0.4 on 2022-05-30 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.DeleteModel(
            name='tipoUsuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
