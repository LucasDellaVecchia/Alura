# Generated by Django 5.0.1 on 2024-01-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0005_fotografia_data_publica"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d"),
        ),
    ]