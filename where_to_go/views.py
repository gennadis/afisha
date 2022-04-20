from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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


def get_place_details(request, id: int):
    place = get_object_or_404(Place, pk=id)
    return HttpResponse(place.title)
