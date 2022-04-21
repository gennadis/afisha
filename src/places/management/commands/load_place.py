import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = "Load place to website"

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str)

    def handle(self, *args, **options):
        place_details = self.get_place_details(url=options["json_url"])
        new_place = self.create_place(place_details)
        for order, image_url in enumerate(place_details["imgs"]):
            self.create_image(order, new_place, image_url)
        print("Done!")

    def get_place_details(self, url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def create_place(self, place_details: dict) -> Place:
        place, _ = Place.objects.update_or_create(
            title=place_details["title"],
            defaults={
                "title": place_details["title"],
                "description_short": place_details["description_short"],
                "description_long": place_details["description_long"],
                "longitude": place_details["coordinates"]["lng"],
                "latitude": place_details["coordinates"]["lat"],
            },
        )
        return place

    def create_image(self, order: int, place: Place, image_url: str):
        image, _ = Image.objects.get_or_create(order=order, place=place)

        response = requests.get(url=image_url)
        response.raise_for_status()

        image.file.save(
            os.path.basename(response.url), ContentFile(response.content), save=True
        )
        return image
