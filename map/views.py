from django.shortcuts import render
from .key import get_key
import googlemaps
import pprint
import time

# Create your views here.


def get_client():
    # define our API_key  
    API_key = get_key()

    # return our client
    return googlemaps.Client(key=API_key)


# places search
def places(request):
    google_client = get_client()
    

    content = {}
    return render(request, 'map/map.html', content)
