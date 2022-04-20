from django.db import models


class Place(models.Model):
    title = models.CharField(
        verbose_name="Place title",
        max_length=200,
    )
    description_short = models.TextField(
        verbose_name="Short description",
        max_length=500,
        blank=True,
        null=True,
    )
    description_long = models.TextField(
        verbose_name="Long description",
        max_length=5000,
        blank=True,
        null=True,
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    def get_place_images(self) -> list[str]:
        return [image.file.url for image in self.images.all()]

    def __str__(self) -> str:
        return f"{self.title} @ {self.longitude}, {self.latitude}"


class Image(models.Model):
    order = models.PositiveSmallIntegerField(
        verbose_name="Image order",
        default=0,
    )
    place = models.ForeignKey(
        to=Place,
        on_delete=models.CASCADE,
        related_name="images",
    )
    file = models.ImageField(
        verbose_name="Place photo",
        upload_to="places/",
    )

    class Meta:
        ordering = ["place", "order"]

    def __str__(self) -> str:
        return f"{self.order} {self.place}"
