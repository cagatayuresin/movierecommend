# Generated by Django 4.1 on 2022-08-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("tt", models.CharField(max_length=10, verbose_name="TT")),
                ("url", models.CharField(max_length=37, verbose_name="url")),
                ("title", models.CharField(max_length=60, verbose_name="Title")),
                (
                    "IMDb_point",
                    models.CharField(max_length=3, verbose_name="IMDB Point"),
                ),
                ("director", models.CharField(max_length=40, verbose_name="Director")),
                ("genres", models.CharField(max_length=30, verbose_name="Genres")),
                ("year", models.CharField(max_length=4, verbose_name="Year")),
                ("duration", models.CharField(max_length=3, verbose_name="Duration")),
            ],
        ),
    ]
