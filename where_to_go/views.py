import json

from django.shortcuts import render

from places.models import Place


def index(request):
    places_collection = {
        "type": "FeatureCollection",
        "features": [],
    }

    for place in Place.objects.all():
        place_features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.latitude, place.longitude],
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json",
            },
        }
        places_collection["features"].append(place_features)

    return render(
        request,
        template_name="index.html",
        context={"places_collection": places_collection},
    )
