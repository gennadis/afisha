# Generated by Django 4.0.4 on 2022-04-20 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={"ordering": ["order", "place"]},
        ),
        migrations.AlterField(
            model_name="image",
            name="order",
            field=models.PositiveSmallIntegerField(
                db_index=True, default=0, verbose_name="Image order"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
            ),
        ),
    ]
