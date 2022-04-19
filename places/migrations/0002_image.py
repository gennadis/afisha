# Generated by Django 4.0.4 on 2022-04-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "order",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Image order"
                    ),
                ),
                (
                    "file",
                    models.ImageField(
                        upload_to="media/places", verbose_name="Place photo"
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="places.place"
                    ),
                ),
            ],
            options={"ordering": ["place", "order"]},
        ),
    ]
