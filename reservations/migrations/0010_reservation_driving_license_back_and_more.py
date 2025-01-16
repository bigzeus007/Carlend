# Generated by Django 5.1.4 on 2025-01-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0009_alter_reservation_client_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="driving_license_back",
            field=models.FileField(
                blank=True, null=True, upload_to="documents/driving_license/back/"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="driving_license_front",
            field=models.FileField(
                blank=True, null=True, upload_to="documents/driving_license/front/"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="id_card_back",
            field=models.FileField(
                blank=True, null=True, upload_to="documents/id_card/back/"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="id_card_front",
            field=models.FileField(
                blank=True, null=True, upload_to="documents/id_card/front/"
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="client_license_plate",
            field=models.CharField(max_length=20, verbose_name="Plaque"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="client_vehicle_date",
            field=models.DateField(verbose_name="Mise en circulation"),
        ),
    ]
