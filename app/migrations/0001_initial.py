# Generated by Django 4.0.4 on 2022-06-13 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estadoDespacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoDespacho', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_estadoDesp',
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('isSuscrito', models.BooleanField()),
            ],
            options={
                'db_table': 'db_Suscripcion',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
            options={
                'db_table': 'db_producto',
            },
        ),
        migrations.CreateModel(
            name='Items_Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'db_table': 'db_items_carrito',
            },
        ),
        migrations.CreateModel(
            name='historialCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('fechaCompra', models.DateField()),
                ('precio', models.CharField(max_length=20)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
            options={
                'db_table': 'db_historial',
            },
        ),
        migrations.CreateModel(
            name='despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('fechaCompra', models.DateField()),
                ('fechaEstimadaEntrega', models.DateField()),
                ('precio', models.CharField(max_length=20)),
                ('estadoDespacho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadodespacho')),
            ],
            options={
                'db_table': 'db_despacho',
            },
        ),
    ]
