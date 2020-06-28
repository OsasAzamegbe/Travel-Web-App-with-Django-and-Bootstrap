from django.shortcuts import render
from key import get_key
import googlemaps
import pprint
import time

# Create your views here.


def get_client():
    # define our API_key  
    API_key = get_key()

    # return our client
    return googlemaps.Client(key=API_key)


google_client = get_client()

# places search


def places(request):
    content = {}
    return render(request, 'map/map.html', content)
