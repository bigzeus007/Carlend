# Generated by Django 5.1.4 on 2024-12-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0005_remove_reservation_deleted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="reservation",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
