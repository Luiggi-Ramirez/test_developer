# Generated by Django 4.2.2 on 2023-06-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConcesionesMaritimas",
            fields=[
                (
                    "n",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("n_concesion", models.CharField(max_length=10)),
                ("tipo_concesion", models.CharField(max_length=100)),
                ("comuna", models.CharField(max_length=20)),
                ("lugar", models.CharField(max_length=120)),
                ("n_rs_ds", models.CharField(max_length=20)),
                ("tipo_tramite", models.CharField(max_length=120)),
                ("concesionario", models.CharField(max_length=120)),
                ("tipo_vigencia", models.CharField(max_length=120)),
            ],
        ),
    ]
