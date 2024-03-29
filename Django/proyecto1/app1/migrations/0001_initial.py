# Generated by Django 4.1 on 2022-09-16 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30)),
                ("descripcion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Direccion_cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calle", models.CharField(max_length=30)),
                ("numero", models.CharField(max_length=5)),
                ("comuna", models.CharField(max_length=100)),
                ("ciudad", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Direccion_proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calle", models.CharField(max_length=30)),
                ("numero", models.CharField(max_length=5)),
                ("comuna", models.CharField(max_length=100)),
                ("ciudad", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30)),
                ("precio", models.FloatField()),
                ("stock", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Telefonos_clientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("telefono", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Venta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descuento", models.FloatField()),
                ("fecha", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=30)),
                ("web", models.URLField()),
                ("telefono", models.IntegerField(max_length=10)),
                (
                    "direccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.direccion_proveedor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto_venta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.IntegerField()),
                (
                    "Producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.producto"
                    ),
                ),
                (
                    "Venta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.venta"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=30)),
                (
                    "direccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.direccion_cliente",
                    ),
                ),
                (
                    "telefono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.telefonos_clientes",
                    ),
                ),
            ],
        ),
    ]
