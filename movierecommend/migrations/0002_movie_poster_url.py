# Generated by Django 4.1 on 2022-08-15 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movierecommend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="poster_url",
            field=models.CharField(default="*", max_length=200, verbose_name="Poster"),
            preserve_default=False,
        ),
    ]