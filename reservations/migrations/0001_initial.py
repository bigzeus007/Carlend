# Generated by Django 5.1.4 on 2024-12-29 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vehicles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("client_name", models.CharField(max_length=100)),
                ("client_license_plate", models.CharField(max_length=20)),
                ("client_vehicle_date", models.DateField()),
                ("commercial_advisor", models.CharField(max_length=100)),
                ("service_advisor", models.CharField(max_length=100)),
                (
                    "criticality",
                    models.CharField(
                        choices=[
                            ("low", "Faible"),
                            ("medium", "Moyen"),
                            ("high", "Critique"),
                        ],
                        max_length=20,
                    ),
                ),
                ("reservation_date", models.DateField()),
                (
                    "reservation_duration",
                    models.PositiveIntegerField(help_text="Durée en jours"),
                ),
                ("reasons", models.TextField()),
                ("is_assigned", models.BooleanField(default=False)),
                (
                    "assigned_vehicle",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vehicles.vehicle",
                    ),
                ),
            ],
        ),
    ]