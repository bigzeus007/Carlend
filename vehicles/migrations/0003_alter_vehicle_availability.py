# Generated by Django 5.1.4 on 2025-01-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0002_alter_vehicle_availability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="availability",
            field=models.CharField(
                choices=[
                    ("disponible", "Disponible"),
                    ("réservé", "Réservé"),
                    ("indisponible", "Indisponible"),
                ],
                default="disponible",
                max_length=15,
            ),
        ),
    ]
