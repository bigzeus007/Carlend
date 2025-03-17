# Generated by Django 5.1.5 on 2025-03-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='fuel_level',
            field=models.PositiveIntegerField(default=50, verbose_name='Niveau de Carburant'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(default=12345678912345678, max_length=17, unique=True, verbose_name='Numéro de Châssis'),
            preserve_default=False,
        ),
    ]
