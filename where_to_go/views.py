import json

from django.shortcuts import render

from places.models import Place


def index(request):
    places_collection = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [37.62, 55.793676]},
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json",
                },
            },
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [37.64, 55.753676]},
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json",
                },
            },
        ],
    }

    return render(
        request,
        template_name="index.html",
        context={"places_collection": places_collection},
    )
