# Generated by Django 5.0.1 on 2024-01-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="legenda",
            field=models.CharField(max_length=150),
        ),
    ]